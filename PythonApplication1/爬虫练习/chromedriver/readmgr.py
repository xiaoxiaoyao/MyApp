# -*- coding: utf-8 -*-
'''
下载网页上的表格数据，然后存系统，简单点，在readmgr
'''
__author__ = 'lai yao (lake.lai)'

import os,sys,time
from selenium import webdriver
URL =''
downloadDir='/Users/laiyao/Downloads/download/'
os.chdir(downloadDir)
print('当前目录',os.getcwd())
if True:
    option = webdriver.ChromeOptions()#自定义设置
    prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': downloadDir}
    option.add_experimental_option('prefs', prefs)
    option.add_argument('--user-data-dir=/Users/laiyao/Library/Application Support/Google/Chrome')
    option.add_argument('--process-per-site') #每个站点使用单独进程
    option.add_argument('--lang=zh-CN') #设置语言为简体中文

    chromedriver='/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chromedriver,chrome_options=option)
    time.sleep(1)
    driver.get(URL)
    time.sleep(20)

for i in url:
    time.sleep(11)
    print(i)
    driver.get(i)