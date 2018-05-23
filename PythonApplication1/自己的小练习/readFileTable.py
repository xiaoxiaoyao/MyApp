#-*- coding: UTF-8 -*-   
  
''''' 
接口开发：从本地读取数据（xls，csv，txt，xlsx）,部分格式有问题的对付掉,计算结果,再写入远程数据库
1、读取指定目录下的所有文件 
2、根据读取文件类型（都是表格文件），读取成SQL可以识别的格式。部分格式有问题的需要对付掉
3、导入SQL
'''  

# 读取文件必备
import os,sys
# AttributeError: 'NoneType' object has no attribute 'fileno'补丁

# 输出靠谱日志必备
import logging
logging.basicConfig(level=logging.DEBUG)

# 为了让Python能够高效率处理表格数据，我们使用一个非常优秀的数据处理框架Pandas。
# 另外，利用pandas.DataFrame.to_sql写入数据库。
import pandas as pd
import numpy as np

# 导入SQL用包
import pymssql

# SQL连接单独写
def conn(host =".",database ="test",user="sa",password="123"):
    conn = pymssql.connect(host=host,database=database,user=user,password=password)
    return conn.cursor()

# 遍历指定目录，显示目录下的所有文件名  
def eachFile(path):  
    pathDir =  os.listdir(path)
    pathFile=[]
    for allDir in pathDir:  
        child = os.path.join(path, allDir)
        logging.info("目录下发现文件：" + child)
        pathFile.append(child)
    return pathFile

# 用panda读取文件
def readFile(type,filepath):
    # 通过匿名函数实现Switch/Case
    return {
            'csv': lambda x: pd.read_csv(x,encoding='gb2312',sep=",|\t",engine='python'), # 吐槽一句，不知道为什么csv格式分隔符会有空格和逗号2种格式，坑爹啊。
            'txt': lambda x: pd.read_csv(x,encoding='gb2312',sep="\t"),
            'xls': lambda x: pd.read_excel(x), 
            'lsx': lambda x: pd.read_excel(x), # lsx = xlsx
    }[type](filepath)



if __name__ == '__main__':  
    # TODO：测试时写死文件路径，实际运行时需要改，最好能够自动化
    fileInPath = "D:\\test"  
    # 连数据库
    cur=conn(host =".",database ="test",user="sa",password="123")
    #TODO 不知道数据库长什么样，后面没法写了
