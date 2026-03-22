#!/usr/bin/python3
# -*- coding:utf8 -*-
''''' 
接口开发：从本地读取数据（xls，csv，txt，xlsx）,部分格式有问题的对付掉,计算结果,再写入远程数据库
1、读取指定目录下的所有文件 
2、根据读取文件类型（都是表格文件），读取成SQL可以识别的格式。部分格式有问题的需要对付掉
3、导入SQL
'''  
## 基本配置START ##
# 配置文件路径
path='D:\\config.txt' 

# TODO：测试时写死文件路径，实际运行时需要改，最好能够自动化
fileInPath = "D:\\test" 

#数据库连接基本信息，详见 def conn
sqlType="mssql"
pysql="pymssql"
host ="127.0.0.1"
defaultDatabase,defaultTableName = 'test','test' # 默认导入数据库名字，以防万一匹配不上的情况。注意默认表名为文件名
database,tableName =defaultDatabase,defaultTableName ## 该变量值由配置文件决定，决定导入的哪个数据库的哪个表
user="sa"
password="123"

## 基本配置END ##

## 导入包和打补丁START ##

# 处理字符串必备
import string,json

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
pd.options.display.encoding='utf-8'
pd.set_option('display.unicode.east_asian_width', True)

# 导入SQL用包
import sqlalchemy,pymssql
from sqlalchemy import create_engine

## 导入包和打补丁END ##


## 读取配置文件 START ##
import configparser as ConfigParser
'''
# 配置文件示例
[这里写啥都行]
head=文件名开头不变的部分
database=导入哪个数据库
tableName=数据库表名字叫什么
'''
cf=ConfigParser.ConfigParser()
cf.read(path, encoding='utf-8')
filenameConfigInfo={} # 最终效果：{'年竞争力外单时效_快件环节延误_7日_': {'database': 'test', 'tableName': '年竞争力外单时效_快件环节延误_7日_'}}
for i in cf.sections() :
	filenameConfigInfo[cf.items(i)[0][1]]={'database': cf.items(i)[1][1], 'tableName': cf.items(i)[2][1]}

## 读取配置文件 END ##

def conn(sqlType="mssql",pysql="pymssql",host ="127.0.0.1",database ="test",user="sa",password="123"):
    '''
    # 现代化的数据库链接方式
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
    # echo=True是调试模式'''
    return create_engine(sqlType+'+'+pysql+'://'+user+':'+password+'@'+host+'/'+database+'?charset=utf8', echo=True)
    # 传统的数据链接模式：
    # def conn(host =".",database ="test",user="sa",password="123"):
    #     return pymssql.connect(host=host,database=database,user=user,password=password)

def filenameConfig(filename='18年竞争力外单时效_快件环节_延误日明细_20180713144930.csv',Config={'18年竞争力外单时效_快件环节_延误日明细_':{'database':'test','tableName':'快件环节_延误日明细T1'}}):
    '''# 根据文件名匹配对应配置文件数据，匹配不到就raise ImportError'''
    for key in Config:
        print(key,filename)
        if filename.find(key) != -1:
            return Config[key]
    raise ImportError('文件找不到对应的配置信息，请检查配置文件。注意配置文件写法。文件名：'+filename)
  
def eachFile(path = "D:\\test" ):  
    '''# 遍历指定目录，显示目录下的所有文件名'''
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

def readFile(file={'fname': '验收及时率（总记录445）', 'dirname': 'D:\\test', 'filename': '验收及时率（总记录445）.xls', 'fename': '.xls', 'fulldir': 'D:\\test\\验收及时率（总记录445）.xls'}):
    '''# 用panda读取文件+改名'''
    type,fulldir=file['fename'],file['fulldir']
    # 导入文件改名需求
    try:
        os.rename(fulldir,file['dirname']+"\\【导入中】"+file['filename'].strip(string.digits))
    except IOError as identifier:
        logging.error("文件改名出现异常IOError"+str(identifier))
    else:
        file['filename']="【导入中】"+file['filename'].strip(string.digits)
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
            '.xlsx': lambda x: pd.read_excel(x, encoding='utf-8', errors='ignore'), 
    }.get(type)(open(fulldir))

def readFileToSQL(file):
    '''业务代码，读取文件，根据文件名判断对应数据库和表名，并写入数据库。
    # 读取的文件存数组里，以后说不定有用'''
    logging.info("正在读取文件：readFile(file)"+str(file))
    file['df']=readFile(file) # 传指针不传数值，方便函数改文件名后能返回正确文件名，如果这个程序长时间运行占内存太大，可以DEL掉这个变量
    # 此处需要按文件名决定导入的数据库和表名，万一匹配不上，就按默认处理
    try:
        info=filenameConfig(filename=file['fname'],Config=filenameConfigInfo)
    except ImportError as identifier:
        logging.warning('文件名不在匹配列表中，按默认文件名处理，导入以下数据库的数据表：'+defaultDatabase+file['fname'])
        logging.warning(identifier)
        database,tableName=defaultDatabase,file['fname']
    else:
        database,tableName=info['database'],info['tableName']
        logging.info('读取正常，信息为'+file['fname']+'数据库信息：'+database+tableName)
    # 连数据库，这里需求改过，根据不同文件名，要链接不同数据库
    logging.debug("即将开始写数据库,sqlType:"+sqlType+",pysql引擎："+pysql+",HOST"+host+",database数据库名称："+database+",user用户名"+user)
    engine=conn(sqlType,pysql,host,database,user,password)
    # 批量入数据库，使用pandas IO Tools，参考http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.to_sql.html?chunksize=1000的意思是分块导入，最大块大小1000
    file['df'].to_sql(tableName,engine, if_exists='append', chunksize=1)
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    # 如果不存在则创建目录
    if not os.path.exists(file['dirname']+"\\【导入成功】"):
        os.makedirs(file['dirname']+"\\【导入成功】") 
    os.rename(file['fulldir'],file['dirname']+"\\【导入成功】\\"+file['filename'])
    pass
if __name__ == '__main__':   
    # 遍历指定目录，统计目录下所有文件
    fileList=eachFile(fileInPath)
    # 批量读文件，批量入数组
    fileArray=[]
    readError=[]
    isReadError=False
    for file in fileList:
        # 开始读取文件并写入数据库，读取后挪文件位置
        try:
            readFileToSQL(file)
        except UnicodeDecodeError as identifier: # 常见错误：文件编码错误，目前还没办法解决，比较坑爹
            # 反馈读取不了的文件，同时统计一下
            logging.error("文件读取失败（文件编码不对）"+str(identifier))
            readError.append((file,identifier))
            isReadError=True
            try:
                # 判断路径是否存在
                # 存在     True
                # 不存在   False
                # 如果不存在则创建目录
                if not os.path.exists(file['dirname']+"\\【导入失败】"):
                    os.makedirs(file['dirname']+"\\【导入失败】") 
                os.rename(file['fulldir'],file['dirname']+"\\【导入失败】\\"+file['filename'])
            except PermissionError as identifier:
                pass
            finally:
                pass
        except PermissionError as identifier: # 常见错误：文件正在使用中，重启一下Python就OK
            logging.error("文件读取失败（文件正在使用中，建议重启试试），具体是这个文件："+file['dirname']+"系统提示错误信息为："+str(identifier))
            readError.append((file,identifier))
            isReadError=True
        else:
            logging.info("【读取文件成功】："+str(file)) 
            print("【读取文件成功】："+file)
        finally:
            logging.debug("读取文件完毕："+str(file))  
            # 如果程序长时间运行容易出错，就取消下面这一行的注释
            # del file          
    if isReadError:
        # 输出导出失败记录
        print("# 输出导出失败记录"+str(readError))
        logging.error("# 输出导出失败记录"+str(readError))
    else:
        print("导入成功")
