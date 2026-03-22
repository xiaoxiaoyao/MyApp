#!/usr/bin/env python3# -*- coding: utf-8 -*-
# # 写个工具，方便自己
# # function：定时抓取免费代理IP,并检查可用性，可用proxy存入数据库供业务方调用获取
# # Author:xiaoxiaoyao
# # date: 2018-09-14
# # password='123qweasdzxc' 为随意输入的密码，绝对非真实使用的密码。 user='root'为标准用户名，绝非实际使用用户名
from bs4 import BeautifulSoup
import traceback, pymysql, threading, time,requests

arrIpList = []

def GrabIpProxy():
    '''
    *@Function【爬取IpProxy】
    *@Request: 请求 [in]
    *   param1 int iReqGetNum: 请求获取代理量
    *@Response：响应 [out]
    *   param1 int iFinalGetNum: 最终获取代理量
    *@Return：返回值 int : 0(成功) 其它失败
    '''
    arrIpList = []
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' }# macOS下的 Chrome 浏览器
    url = 'http://www.xicidaili.com/nn/1'# 获取代理列表
    #url = 'http://www.baidu.com'
    res = requests.get(url, headers=header)
    if res.status_code == 200: # 访问正常正常
        soup = BeautifulSoup(res.text, 'lxml')
        ips = soup.findAll('tr')
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_port = tds[1].contents[0] + ":" + tds[2].contents[0]
            arrIpList.append(ip_port)            #后续加上代理可用校验，非可用踢出代理池
            print(ip_port)
    #计算列表量
    return arrIpList
def checkProxyIP(desUrl = 'http://www.baidu.com', ipProxy="127.0.0.1", iTimeout=3, feature=""):
    '''
    *@Function【测试ipProxy是否可用】（单个IP检测）
    *@Request: 请求 [in]
    *   param1 String desUrl: 测试目的地址
    *   param2 String ipProxy:代理IP端口
    *   param3 int iTimeout:超时时间
    *   param4 String feature:目的地址特征
    *@Response：响应 [out]
    *   param1 int iFinalGetNum: 最终获取代理量
    *@Return：返回值 ：成功返回代理Proxy 失败返回空
    '''
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' }# macOS下的 Chrome 浏览器
    proxies = {'http': 'http://' + ipProxy}        #组装代理
    res = None  # 声明
    # exMsg = None
    try:    #确认带来iPaddress 3秒内能否ping通
        res = requests.get(url=desUrl, headers=header, proxies=proxies, timeout=iTimeout)
        # res = requests.get(desUrl, proxies=proxies, timeout=iTimeout)  # 代理方式请求，防止反爬虫
        # soup = BeautifulSoup(res.text, 'lxml')
        #feature=""
        #print(soup.findAll(feature))
    except:
        # exMsg = '* ' + traceback.format_exc()
        return -1
    if res.status_code != 200:
        return -1
    if res.text.find(feature) < 0:
        return -1
    return 0
def CheckIpProxyTimer(arrIp='127.0.0.1'):
    # //TODO
    #测试地址
    #feature = 'xxx'                 #目标网页的特征码, 暂时不启用
    pass

def setProxy(ipProxy='127.0.0.1', isOK="N"):
    # //TODO
    print(ipProxy,isOK)
    pass

if __name__ == '__main__':    #0、爬取免费代理IP
    #0、爬取免费代理IP
    arrIpList = GrabIpProxy()    
    #1、启动定时线程，定时测试并清洗数据库代理IP
    timer = threading.Timer(3600, CheckIpProxyTimer)
    timer.start()    
    #2、设置定时器失效时间
    time.sleep(5)
    timer.cancel()      #5秒后停止定时器，程序可一直执行