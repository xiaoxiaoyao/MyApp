# -*- coding: utf-8 -*-
'''
下载网页上的表格数据，然后存系统，简单点
'''
__author__ = 'lai yao (lake.lai)'

import os,sys,time
from selenium import webdriver
if True:
    option = webdriver.ChromeOptions()#自定义设置
    option.add_argument('--user-data-dir=/Users/laiyao/Library/Application Support/Google/Chrome')
    option.add_argument('--process-per-site') #每个站点使用单独进程
    option.add_argument('--lang=zh-CN') #设置语言为简体中文

    chromedriver='/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chromedriver,chrome_options=option)

year=['2015','2016','2017','2018']
mouth=['01','02','03','04','05','06','07','08','09','10','11','12']
URL =''
def gressURL():
    startURL = input("first start URL:")
    for i in year:
        for j in mouth :
            yield  startURL + i + j + '.html',i,j

def getTabel(url=URL,driver=driver):
    driver.get(url)
    time.sleep(7)
    return driver.find_element_by_xpath('//*[@id="main"]/div[3]/table').text

def saveData(data='',filename='output'):
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path='/Users/laiyao/Documents'
    fileObj = open(path + '/output/index/' + filename + '.csv','w')
    fileObj.write(data)
    fileObj.close()

def clear():
    driver.close()
    driver.quit()

def work(driver=driver):
    URL = input("input the login in URL")
    driver.get(URL)
    for i in range(20):
        print(i)
        time.sleep(1)
    for URL,i,j in gressURL():
        print(URL,i,j)
        saveData(data=getTabel(url=URL,driver=driver),filename=i+j)
# https://a310.zhulang.com/caiwu/gaofei/index/current_month/201808.html
