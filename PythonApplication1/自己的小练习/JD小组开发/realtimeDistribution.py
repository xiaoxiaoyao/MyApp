
import requests

# 出于数据安全原因，各位各自登录账号后写一下cookies和headers，文件内不方便保存账号密码
data=""
cookies={}
headers={}

# Only Python 3.6 is supported.
# requests-html 是基于现有的框架 PyQuery、Requests、lxml、beautifulsoup4等库进行了二次封装，作者将Requests设计的简单强大的优点带到了该项目中。

# 将cookie 转换成字典格式
def strToDictionary(b):
    d ={}#初始化字典变量  
    for line in b.split(';'):#按照字符：进行划分读取  
        #其设置为1就会把字符串拆分成2份 
        key,value = line.split('=',1)
        d[key] = value
    return d

def HARToDictionary(b):
    d ={}#初始化字典变量  
    for line in b:#分割 
        #其设置为1就会把字符串拆分成2份 
        d[line['name']]=line[ 'value']
    return d

# 这里是我标记JSON的那几个，直接解决
response = requests.get('http://zw.ql.jd.com/wholeProcess/query?orgId=0&proCode=&date=Tue+May+29+2018+00%3A00%3A00+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)', data=data,cookies=cookies,headers=headers)
response.json()["allWaybillAmount"]

# 这里是我标记命中的那几个，用下载Excel的方式解决
# showTime=2018/05/30 03:15:37&isToday=1&orgId=0&orgName=全国&proCode=&proName=全部省公司&areaCode=&areaName=全部片区&partCode=&partName=全部分区&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=全部市&dimensionType=1
response = requests.get('http://zw.ql.jd.com/realtimeDistribution/export?showTime=2018/05/30%2003:15:37&isToday=1&orgId=0&orgName=%25E5%2585%25A8%25E5%259B%25BD&proCode=&proName=%25E5%2585%25A8%25E9%2583%25A8%25E7%259C%2581%25E5%2585%25AC%25E5%258F%25B8&areaCode=&areaName=%25E5%2585%25A8%25E9%2583%25A8%25E7%2589%2587%25E5%258C%25BA&partCode=&partName=%25E5%2585%25A8%25E9%2583%25A8%25E5%2588%2586%25E5%258C%25BA&siteId=&siteName=&provinceId=&provinceName=&cityId=&cityName=%25E5%2585%25A8%25E9%2583%25A8%25E5%25B8%2582&dimensionType=1', data=data,cookies=cookies,headers=headers)
print(response.content)