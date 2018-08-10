#!/usr/bin/env Python
# coding=utf-8
''''' 
接口开发：从本地读取数据（xls，csv，txt，xlsx）,部分格式有问题的对付掉,计算结果,再写入远程数据库
1、读取指定目录下的所有文件 
2、根据读取文件类型（都是表格文件），读取成SQL可以识别的格式。部分格式有问题的需要对付掉
3、导入SQL

以下表格含有二级表头：
订单出库量统计（总记录*）
每日病单量统计（总记录*）
内配收货监控汇总（总记录*）
'''  
## 基本配置START ##
# TODO：测试时写死文件路径，实际运行时需要改，最好能够自动化
fileInPath = "D:\\test" 

#数据库连接基本信息，详见 def conn
sqlType="mssql"
pysql="pymssql"
host ="127.0.0.1"
database ="test"
user="sa"
password="123"

## 基本配置END ##

## 导入包和打补丁START ##

# 处理字符串必备
import string

# 读取文件必备
import os,sys
# AttributeError: 'NoneType' object has no attribute 'fileno'补丁
sys.__stdout__ = sys.stdout

# 输出靠谱日志必备
import logging
#是否开启debug？根据事件的轻重可分为以下几个级别：
# DEBUG： 详细信息，通常仅在诊断问题时才受到关注。整数level=10
# INFO： 确认程序按预期工作。整数level=20
# WARNING：出现了异常，但是不影响正常工作.整数level=30
# ERROR：由于某些原因，程序 不能执行某些功能。整数level=40
# CRITICAL：严重的错误，导致程序不能运行。整数level=50
# 默认的级别是WARNING,也就意味着只有级别大于等于的才会被看到，跟踪日志的方式可以是写入到文件中，也可以直接输出到控制台。
logging.basicConfig(level=logging.INFO)

# 为了让Python能够高效率处理表格数据，我们使用一个非常优秀的数据处理框架Pandas。
# 另外，利用pandas.DataFrame.to_sql写入数据库。
import pandas as pd
import numpy as np

# 导入SQL用包
import sqlalchemy,pymssql
from sqlalchemy import create_engine

## 导入包和打补丁END ##

# 现代化的数据库链接方式
def conn(sqlType="mssql",pysql="pymssql",host ="127.0.0.1",database ="test",user="sa",password="123"):
    # pymssql.create_engine是数据库引擎
    # ('mysql+mysqldb://root:password@localhost:3306/databasename?charset=utf8')的解释
    # mysql是要用的数据库
    # mysqldb是需要用的接口程序
    # root是数据库账户
    # password是数据库密码
    # localhost是数据库所在服务器的地址，这里是本机
    # 3306是mysql占用的端口
    # elonuse是数据库的名字
    # charset=utf8是设置数据库的编码方式，这样可以防止latin字符不识别而报错
    # echo=True是调试模式
    return create_engine(sqlType+'+'+pysql+'://'+user+':'+password+'@'+host+'/'+database+'?charset=utf8', echo=True)

# 传统的数据链接模式：
# def conn(host =".",database ="test",user="sa",password="123"):
#     return pymssql.connect(host=host,database=database,user=user,password=password)

# 遍历指定目录，显示目录下的所有文件名  
def eachFile(path):  
    pathDir =  os.listdir(path)
    pathFile=[]
    for allDir in pathDir:  
        child = os.path.join(path, allDir)
        logging.info("目录下发现文件：" + child)
        tmp={}
        tmp['fulldir']=child
        tmp['dirname'],tmp['filename']=os.path.split(child)
        tmp['fname'],tmp['fename']=os.path.splitext(tmp['filename'])
        pathFile.append(tmp)
    return pathFile

# 用panda读取文件+改名
def readFile(file):
    type,fulldir=file['fename'],file['fulldir']
    # 导入文件改名需求
    try:
        os.rename(fulldir,file['dirname']+"\\【导入中】"+file['filename'].rstrip(string.digits))
    except IOError as identifier:
        logging.error("文件改名出现异常IOError"+str(identifier))
    else:
        file['filename']="【导入中】"+file['filename'].rstrip(string.digits)
        file['fulldir']=file['dirname']+'\\'+file['filename']
        type,fulldir=file['fename'],file['fulldir']
        logging.info("文件改名成功"+str(file))
    finally:
        logging.info("正在读取文件：readFile(type,fulldir)"+str(file))
    
    # 通过匿名函数实现Switch/Case
    return {
            '.csv': lambda x: pd.read_csv(x,encoding='gb2312',sep=",|\t",engine='python'), # 吐槽一句，不知道为什么csv格式分隔符会有空格和逗号2种格式，坑爹啊。
            '.txt': lambda x: pd.read_csv(x,encoding='gb2312',sep=",|\t",engine='python'),
            '.xls': lambda x: pd.read_excel(x,encoding='gbk'),
            '.xlsx': lambda x: pd.read_excel(x,encoding='utf-8'), 
    }.get(type)(open(fulldir))

if __name__ == '__main__':   
    # 连数据库
    engine=conn(sqlType,pysql,host,database,user,password)
    # 遍历指定目录，统计目录下所有文件
    fileList=eachFile(fileInPath)
    # 批量读文件，批量入数组
    fileArray=[]
    readError=[]
    isReadError=False
    for file in fileList:
        # 开始读取文件并写入数据库
        try:
            # 读取的文件存数组里，以后说不定有用
            logging.info("正在读取文件：readFile(file)"+str(file))
            file['df']=readFile(file) # 传指针不传数值，方便函数改文件名后能返回正确文件名
        except UnicodeDecodeError as identifier:
            # 反馈读取不了的文件，同时统计一下
            logging.error("文件读取失败（文件编码不对）"+str(identifier))
            readError.append(file)
            isReadError=True
            # 判断路径是否存在
            # 存在     True
            # 不存在   False
            # 如果不存在则创建目录
            if not os.path.exists(file['dirname']+"\\【导入失败】"):
                os.makedirs(file['dirname']+"\\【导入失败】") 
            os.rename(file['fulldir'],file['dirname']+"\\【导入失败】\\"+file['filename'])
        else:
            logging.debug("即将开始写数据库,sqlType:"+sqlType+",pysql引擎："+pysql+",HOST"+host+",database数据库名称："+database+",user用户名"+user)
            # 批量入数据库，使用pandas IO Tools，参考http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.to_sql.html?chunksize=1000的意思是分块导入，最大块大小1000
            file['df'].to_sql(file['fname'],engine, if_exists='append', chunksize=1)
            # 判断路径是否存在
            # 存在     True
            # 不存在   False
            # 如果不存在则创建目录
            if not os.path.exists(file['dirname']+"\\【导入成功】"):
                os.makedirs(file['dirname']+"\\【导入成功】") 
            os.rename(file['fulldir'],file['dirname']+"\\【导入成功】\\"+file['filename'])
        finally:
            logging.info("读取文件完毕："+str(file))            
    if isReadError:
        # 输出导出失败记录
        logging.error("# 输出导出失败记录")
        logging.error(readError)
    else:
        print("导入成功")


# 单元测试代码
import unittest
class TestMathFunc(unittest.TestCase):
    '''Test 自己'''
    def setUp(self):
        '''开始测试时使用setUp设置环境，注意每个测试用例都会跑一遍'''
        debug,fileInPath=True,"D:\\test"
        print('unittest start','debug,fileInPath=',debug,fileInPath)
        # AttributeError: 'NoneType' object has no attribute 'fileno'补丁
        # import os,sys
        # sys.__stdout__ = sys.stdout
        logging.basicConfig(level=logging.DEBUG) if debug else logging.basicConfig(level=logging.WARNING)


    def tearDown(self):
        '''结束测试时使用tearDown清理环境，注意每个测试用例都会跑一遍'''
        print('unittest ended')
