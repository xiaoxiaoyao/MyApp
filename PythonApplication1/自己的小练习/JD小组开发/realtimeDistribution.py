
# 第一步：初始化变量、导入各种包

# 开发过程中，开启debug
debug=True

# 输出文件文件名
outfile='outfile.xlsx'

# 青龙系统网站域名
host='http://zw.ql.jd.com/'

# 处理时间日期必备
import datetime,time
now = datetime.datetime.now()
# 想知道now怎么用吗？看右边→    print(now,now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)  
# strftime() and strptime() Behavior 参考https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# 【重要】cookiesText变量记录了cookies，任何时候请勿分享传播
cookiesText='cookies字段保密数据脱敏上传保密数据脱敏上传保密数据脱敏上传'

# 抓取结果1，结果1：	如下图，每小时的单量呈现，URL
    # 来源页：青龙智网-配送整体运营全景图-配送&集运 ./index
    # URL解码以后，GET是?orgId=0&proCode=&date=Tue May 29 2018 00:00:00 GMT+0800 (中国标准时间)
urlData1=host + 'wholeProcess/query?orgId=0&proCode=&date='+ now.strftime('%a+%b+%d+%Y+%X') +'+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'

# 抓取结果2，结果2：今日截止当前小时的单量呈现，URL
    # 这里是我标记命中的那几个，用下载Excel的方式解决
    # 来源页：青龙智网-可视化数据平台-配送实时运营数据./realtimeDistribution/index
    # URL一次解码以后，GET是?showTime=2018/05/30 03:15:37&isToday=0&orgId=0&orgName=全国&proCode=&proName=全部省公司&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
    # 拼接URL，只要调整日期就可以得到实时数据
urldata2=host + 'realtimeDistribution/export?showTime='+now.strftime("%Y/%m/%d%%20%H:%M:%S")+'&isToday=0&orgId=0&orgName=%25E5%2585%25A8%25E5%259B%25BD&proCode=&proName=%25E5%2585%25A8%25E9%2583%25A8%25E7%259C%2581%25E5%2585%25AC%25E5%258F%25B8&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1'

# # 抓取结果3，结果3：	青龙智网-》实时数据平台-》区域-分区实时监控（选华东，查询后的结果）（原版结果3，错的，注释掉）
# urldata3='./realtime/baseorg/detailExport'
# # 抓取结果3用到的POST数据（原版结果3，错的，注释掉）
# postData3={'showTime': now.strftime("%Y-%m-%d"), 'organCode': '3', 'flag': '3', 'orgId': '3', 'parentCode': '3'}

# 抓取结果3，结果3数据来源比较多，分开写：
    # 结果3-1：站点验货量：从总的站点验货量中得到片区的数据【爬虫】
    # 来源页： ./realtimeDistribution/showRealtimeDistributionDetail?showTime=2018/06/07%2001:57:42&indexKey=siteInspectWaybillAmount&indexName=%25E7%25AB%2599%25E7%2582%25B9%25E9%25AA%258C%25E8%25B4%25A7%25E9%2587%258F&indexData=9,878&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # DATA数据源（Request URL:） ：./realtimeDistribution/exportDetail?showTime=2018/06/07%2001:46:07&isToday=1&indexKey=siteInspectWaybillAmount&indexName=%25E7%25AB%2599%25E7%2582%25B9%25E9%25AA%258C%25E8%25B4%25A7%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # URL一次解码： ?showTime=2018/06/07 01:46:07&isToday=1&indexKey=siteInspectWaybillAmount&indexName=%E7%AB%99%E7%82%B9%E9%AA%8C%E8%B4%A7%E9%87%8F&orgId=3&orgName=%E5%8D%8E%E4%B8%9C&areaCode=&areaName=%E5%85%A8%E9%83%A8%E7%89%87%E5%8C%BA&partCode=&partName=%E5%85%A8%E9%83%A8%E5%88%86%E5%8C%BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%E5%85%A8%E9%83%A8%E5%B8%82&dimensionType=1
    # URL二次解码： ?showTime=2018/06/07 01:46:07&isToday=1&indexKey=siteInspectWaybillAmount&indexName=站点验货量&orgId=3&orgName=华东&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
urlData3_1=host + 'realtimeDistribution/exportDetail?showTime='+now.strftime("%Y/%m/%d%%20%H:%M:%S")+'&isToday=1&indexKey=siteInspectWaybillAmount&indexName=%25E7%25AB%2599%25E7%2582%25B9%25E9%25AA%258C%25E8%25B4%25A7%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1'

    # 结果3-2：自营妥投量：华东的妥投情况中得到片区的数据【爬虫】
    # 来源页：./realtimeDistribution/showRealtimeDistributionDetail?showTime=2018/06/07%2001:56:31&indexKey=selfDeliveryStaffDelivered&indexName=%25E8%2587%25AA%25E8%2590%25A5%25E9%2585%258D%25E9%2580%2581%25E5%2591%2598%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&indexData=53&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # DATA数据源（Request URL:） ：./realtimeDistribution/exportDetail?showTime=2018/06/11%2023:41:33&isToday=1&indexKey=selfDeliveryStaffDelivered&indexName=%25E8%2587%25AA%25E8%2590%25A5%25E9%2585%258D%25E9%2580%2581%25E5%2591%2598%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # URL一次解码： ?showTime=2018/06/07 01:56:31&indexKey=selfDeliveryStaffDelivered&indexName=%E8%87%AA%E8%90%A5%E9%85%8D%E9%80%81%E5%91%98%E5%A6%A5%E6%8A%95%E9%87%8F&indexData=53&orgId=3&orgName=%E5%8D%8E%E4%B8%9C&areaCode=&areaName=%E5%85%A8%E9%83%A8%E7%89%87%E5%8C%BA&partCode=&partName=%E5%85%A8%E9%83%A8%E5%88%86%E5%8C%BA&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=%E5%85%A8%E9%83%A8%E5%B8%82&dimensionType=1
    # URL二次解码： ?showTime=2018/06/07 01:56:31&indexKey=selfDeliveryStaffDelivered&indexName=自营配送员妥投量&indexData=53&orgId=3&orgName=华东&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
urlData3_2=host + 'realtimeDistribution/exportDetail?showTime='+now.strftime("%Y/%m/%d%%20%H:%M:%S")+'&isToday=1&indexKey=selfDeliveryStaffDelivered&indexName=%25E8%2587%25AA%25E8%2590%25A5%25E9%2585%258D%25E9%2580%2581%25E5%2591%2598%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1'

    # 结果3-3：众包妥投量：华东的妥投情况中得到片区的数据【爬虫】
    # 来源页：./realtimeDistribution/showRealtimeDistributionDetail?showTime=2018/06/07%2002:01:56&indexKey=crowdDelivered&indexName=%25E4%25BC%2597%25E5%258C%2585%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&indexData=5&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # DATA数据源（Request URL:） ：./realtimeDistribution/exportDetail?showTime=2018/06/07%2002:01:59&isToday=1&indexKey=crowdDelivered&indexName=%25E4%25BC%2597%25E5%258C%2585%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # URL一次解码： ?showTime=2018/06/07 02:01:59&isToday=1&indexKey=crowdDelivered&indexName=%E4%BC%97%E5%8C%85%E5%A6%A5%E6%8A%95%E9%87%8F&orgId=3&orgName=%E5%8D%8E%E4%B8%9C&areaCode=&areaName=%E5%85%A8%E9%83%A8%E7%89%87%E5%8C%BA&partCode=&partName=%E5%85%A8%E9%83%A8%E5%88%86%E5%8C%BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%E5%85%A8%E9%83%A8%E5%B8%82&dimensionType=1
    # URL二次解码： ?showTime=2018/06/07 02:01:59&isToday=1&indexKey=crowdDelivered&indexName=众包妥投量&orgId=3&orgName=华东&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
urlData3_3=host + 'realtimeDistribution/exportDetail?showTime='+now.strftime("%Y/%m/%d%%20%H:%M:%S")+'&isToday=1&indexKey=crowdDelivered&indexName=%25E4%25BC%2597%25E5%258C%2585%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1'

    # 结果3-4：单独计算其他妥投量=妥投量-自营妥投量-众包妥投量【计算】
pass

    # 结果3-5：妥投量：从总的站点验货量中得到片区的数据【爬虫】
    # 来源页：./realtimeDistribution/showRealtimeDistributionDetail?showTime=2018/06/07%2002:20:26&indexKey=deliveredAmount&indexName=%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&indexData=106&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&isToday=1&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # DATA数据源（Request URL:） ：./realtimeDistribution/exportDetail?showTime=2018/06/07%2002:20:31&isToday=1&indexKey=deliveredAmount&indexName=%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1
    # URL一次解码： ?showTime=2018/06/07 02:20:31&isToday=1&indexKey=deliveredAmount&indexName=%E5%A6%A5%E6%8A%95%E9%87%8F&orgId=3&orgName=%E5%8D%8E%E4%B8%9C&areaCode=&areaName=%E5%85%A8%E9%83%A8%E7%89%87%E5%8C%BA&partCode=&partName=%E5%85%A8%E9%83%A8%E5%88%86%E5%8C%BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%E5%85%A8%E9%83%A8%E5%B8%82&dimensionType=1
    # URL二次解码： ?showTime=2018/06/07 02:20:31&isToday=1&indexKey=deliveredAmount&indexName=妥投量&orgId=3&orgName=华东&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
urlData3_5=host + 'realtimeDistribution/exportDetail?showTime='+now.strftime("%Y/%m/%d%%20%H:%M:%S")+'&isToday=1&indexKey=deliveredAmount&indexName=%25E5%25A6%25A5%25E6%258A%2595%25E9%2587%258F&orgId=3&orgName=%25E5%258D%258E%25E4%25B8%259C&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1'

# 出于数据安全原因，各位各自登录账号后写一下cookies和headers，文件内不方便保存账号密码
data="" # 就是POST上去的东西，其实完全没有必要
url=""
cookies={} # 【重要】就是cookie
headers={} # 就是headers，其实完全没有必要

# 爬虫必备
import requests
import urllib

# 常规必备
import os,sys,io
# AttributeError: 'NoneType' object has no attribute 'fileno'补丁
sys.__stdout__ = sys.stdout

# 处理数据必备
import pandas as pd
import numpy as np
# 一行不管多长都【尽量】给我显示
pd.set_option('display.max_colwidth',50000)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# 输出靠谱日志必备
import logging
logging.basicConfig(level=logging.DEBUG) if debug else logging.basicConfig(level=logging.WARNING)

# 将cookie 转换成字典格式
def strToDictionary(b=""):
    d ={}#初始化字典变量  
    for line in b.split(';'):#按照字符：进行划分读取  
        #其设置为1就会把字符串拆分成2份 
        key,value = line.split('=',1)
        d[key] = value
    return d

def HARToDictionary(b={}):
    d ={}#初始化字典变量  
    for line in b:#分割 
        #其设置为1就会把字符串拆分成2份 
        d[line['name']]=line[ 'value']
    return d

# 给我个URL，还你个JSON
def getDataByDownloadingJSON(url=url,data="",cookies={},headers={}):
    response = requests.get(url, data=data,cookies=cookies,headers=headers)
    # FUTURE【预留】你永远不知道领导想要什么，输出数据一定要全，以避免万一
    return response.json()

# 给我个URL，还你个pandas表格DataFrame 
def getDataByDownloadingExcel(url=url,data=data,cookies=cookies,headers=headers):
    response = requests.get(url, data=data,cookies=cookies,headers=headers)
    logging.debug('# DEBUG 记录下载的文件信息')
    logging.debug(response.headers)
    logging.debug(urllib.parse.unquote(response.headers['Content-Disposition']))
    # FUTURE【预留】你永远不知道领导想要什么，输出数据一定要全，以避免万一
    return pd.read_csv(
        # io.BytesIO，把XXX当作IO流（类似文件）
        io.BytesIO(
            # 正儿八经的二进制输出网页下载的Excel数据
            response.content
            ),encoding='gb2312'
            )

# 给我个URL（POST模式），还你个pandas表格DataFrame
def getDataByPostDownloadingExcel(url=url,data="",cookies={},headers={}):
    response = requests.post(url, data=data,cookies=cookies,headers=headers)
    logging.debug('# DEBUG 记录下载的文件信息')
    logging.debug(response.headers)
    logging.debug(urllib.parse.unquote(response.headers['Content-Disposition']))
    # 和前面一样的套路
    return pd.read_csv(
        io.BytesIO(
            response.content
            ),encoding='gb2312'
            )

# 输出到Excel的套路：
# dataframe: 需要写入excel的数据
# outfile：输出的文件地址
# name: sheet_name的文件名称
import openpyxl
from openpyxl import load_workbook
def excelAddSheet(dataframe, outfile='name.xlsx', name='sheet_name'):
    writer = pd.ExcelWriter(outfile)
    if os.path.exists(outfile) != True:
        dataframe.to_excel(writer, name, index=None)
    else:
        book = load_workbook(writer.path)
        try:
            book.remove(book[name]) # 同名表单自动删除，不需要的话可以注释掉
            print('已覆盖同名sheet'+name)
        except KeyError:
            print('正在添加'+name)
        finally:
            pass
        writer.book = book
        dataframe.to_excel(excel_writer=writer, sheet_name = name, index=None)
    writer.save()
    writer.close()

if __name__ == '__main__':
    cookies=strToDictionary(cookiesText)
    # 读取结果1
    data1=getDataByDownloadingJSON(url=urlData1,data=data,cookies=cookies,headers=headers)
    # 读取结果2
    data2=getDataByDownloadingExcel(url=urldata2,data=data,cookies=cookies,headers=headers)
    # 备注：如果要全国所有区域，就把下面这一个注释掉。
    data2=data2[:4]
    # # 读取结果3（原版结果3，错的，注释掉）
    # data3=getDataByPostDownloadingExcel(url=urldata3,data=postData3,cookies=cookies,headers=headers)
    # 读取结果3-1
    data3_1=getDataByDownloadingExcel(url=urlData3_1,data=data,cookies=cookies,headers=headers)
    # 读取结果3-2
    data3_2=getDataByDownloadingExcel(url=urlData3_2,data=data,cookies=cookies,headers=headers)
    # 读取结果3-3
    data3_3=getDataByDownloadingExcel(url=urlData3_3,data=data,cookies=cookies,headers=headers)
    # # 【计算】结果3-4
    # 
    # 读取结果3-5
    data3_5=getDataByDownloadingExcel(url=urlData3_5,data=data,cookies=cookies,headers=headers)

    # DEBUG数据记录：
    logging.debug('青龙智网-配送整体运营全景图-配送&集运	运单总量' + str(data1["allWaybillAmount"]))
    logging.debug(data2[['区域','终端待验货','站点验货量','妥投量','终端待配送','再投量','自营配送员妥投量','三方快递妥投量','众包妥投量']])
    logging.debug('再投率	再投量/入配单量' + str(data2['再投量']/data1["allWaybillAmount"]) + '其中，入配单量取全国运单总量' + str(data1["allWaybillAmount"]))
    print('【重要】检查一下：青龙智网-配送整体运营全景图-配送&集运	运单总量，是不是' , data1["allWaybillAmount"],'现在时间是',now)
    # 输出结果1，显示+Excel
    print('结果1：	如下图，每小时的单量呈现')
    print('1:终端验货单量（对应字段：终端待验货）')
    print(data2[['区域','终端待验货']])
    print('2:终端妥投单量（对应字段：妥投量）')
    print(data2[['区域','妥投量']])
    print('3:终端自营妥投（对应字段：自营配送员妥投量）')
    print(data2[['区域','自营配送员妥投量']])
    print('4:终端众包妥投（对应字段：众包妥投量）')
    print(data2[['区域','众包妥投量']])
    # 开发预留
    print('*:终端妥投单量（对应字段：自营配送员妥投量+众包妥投量）')
    print([data2[['区域','众包妥投量']],data2['自营配送员妥投量']+data2["众包妥投量"]])
    excelAddSheet(data2[['区域','终端待验货','妥投量','自营配送员妥投量','众包妥投量']],outfile=outfile,name=str(now.hour)+'时单量呈现')
    excelAddSheet(data2,outfile=outfile,name=str(now.hour)+'时单量呈现（备用，所有数据）')

    # 输出结果2
    ranklist=['终端待验货','站点验货量','妥投量','终端待配送','再投量','自营配送员妥投量','三方快递妥投量','众包妥投量','众包妥投量占比']
    print('输出结果2\n三大区各项指标数值：\n',data2[['区域'] + ranklist][:4],'\n华东各项指标排名情况：\n',data2[ranklist].rank()[2:3]) # 华东排第三个，[2:3]切片命中华东.[1:2]
    excelAddSheet(data2[['区域'] +ranklist],outfile=outfile,name='截止当前小时的单量呈现')
    excelAddSheet(data2[['区域'] +ranklist].rank(),outfile=outfile,name='截止当前小时的单量呈现排名')
    
    # # 输出结果3（原版结果3，错的，注释掉）
    # print('输出结果3\n妥投率TOP5（是按什么排名的来着，我忘了。。。随便按站点验货量排序吧）：\n',data3[['片区','站点验货量','站点妥投量(自营)', '站点妥投量(三方)',  '众包妥投量']].sort_values(by="站点验货量",ascending=False))
    # 输出结果3-1
    print('输出结果3\n站点验货量：从总的站点验货量中得到片区的数据\n',data3_1.iloc[:,0:3])
    excelAddSheet(data3_1,outfile=outfile,name='站点验货量')
    # 输出结果3-2
    print('输出结果3\n自营和众包妥投量：华东的妥投情况中得到片区的数据，其中自营\n',data3_2.iloc[:,0:3])
    excelAddSheet(data3_2,outfile=outfile,name='自营妥投')
    # 输出结果3-3
    print('输出结果3\n自营和众包妥投量：华东的妥投情况中得到片区的数据，其中众包\n',data3_3.iloc[:,0:3])
    excelAddSheet(data3_3,outfile=outfile,name='众包妥投')
    # # 输出结果3-4
    # print('输出结果3\n这个是计算出来的\n',data3_1.iloc[:,0:3])
    # 输出结果3-5
    print('输出结果3\n妥投量：从总的站点验货量中得到片区的数据\n',data3_5.iloc[:,0:3])
    excelAddSheet(data3_5,outfile=outfile,name='妥投量')


# 常见问题解决：
# pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 5, saw 4
# 这个是cookie过期了，更新一个新的cookie就OK了
