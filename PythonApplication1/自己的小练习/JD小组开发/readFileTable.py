#!/usr/bin/env Python
# coding=utf-8
debug=0
''''' 
接口开发：从本地读取数据（xls，csv，txt，xlsx）,部分格式有问题的对付掉,计算结果,再写入远程数据库
1、读取指定目录下的所有文件 
2、根据读取文件类型（都是表格文件），读取成SQL可以识别的格式。部分格式有问题的需要对付掉
3、导入SQL
'''  

# 读取文件必备
import os,sys
# AttributeError: 'NoneType' object has no attribute 'fileno'补丁
sys.__stdout__ = sys.stdout

# 输出靠谱日志必备
import logging
logging.basicConfig(level=logging.DEBUG) if debug else logging.basicConfig(level=logging.WARNING)

# 为了让Python能够高效率处理表格数据，我们使用一个非常优秀的数据处理框架Pandas。
# 另外，利用pandas.DataFrame.to_sql写入数据库。
import pandas as pd
import numpy as np

# 导入SQL用包
import sqlalchemy,pymssql
from sqlalchemy import create_engine
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
    return create_engine(sqlType+'+'+pysql+'://'+user+':'+password+'@'+host+'/'+database+'?charset=utf8', echo=debug)

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

# 用panda读取文件
def readFile(type,fulldir):
    # 通过匿名函数实现Switch/Case
    logging.info("readFile(type,fulldir)"+str([type,fulldir]))
    logging.debug("正在读取文件")
    return {
            '.csv': lambda x: pd.read_csv(x,encoding='gb2312',sep=",|\t",engine='python'), # 吐槽一句，不知道为什么csv格式分隔符会有空格和逗号2种格式，坑爹啊。
            '.txt': lambda x: pd.read_csv(x,encoding='gb2312',sep=",|\t",engine='python'),
            '.xls': lambda x: pd.read_excel(x,encoding='gb2312',index=False),
            '.xlsx': lambda x: pd.read_excel(x,encoding='utf-8'), 
    }.get(type)(open(fulldir))

if __name__ == '__main__':  
    # TODO：测试时写死文件路径，实际运行时需要改，最好能够自动化
    fileInPath = "D:\\test"  
    # 连数据库
    engine=conn()
    # 遍历指定目录，统计目录下所有文件
    fileList=eachFile(fileInPath)
    # 批量读文件，批量入数组
    fileArray=[]
    for file in fileList:
        # 读取的文件存数组里，以后说不定有用
        file['df']=readFile(file['fename'],file['fulldir'])
        logging.debug("正在写数据库")
        # 批量入数据库，使用pandas IO Tools，参考http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.to_sql.html?chunksize=1000的意思是分块导入，最大块大小1000
        file['df'].to_sql(file['fname'],engine, if_exists='append', chunksize=500)

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
