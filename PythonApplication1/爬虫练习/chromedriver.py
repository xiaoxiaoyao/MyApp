# -*- coding: utf-8 -*-
'''
我的第一个爬虫

爬自己公司的所有子公司，方便搜索，简单粗暴
'''
__author__ = 'lai yao (lake.lai)'
__date__ ="$2016-04-15 20:56:05$"

import os,time
fileObj = open('C:\\Users\\yaopr\\Source\\Repos\\PythonApplication1\\OUTPUT\\output.txt','w') 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def chrome(url):
    driver.get(url)
    data=driver.find_element_by_css_selector(".col-md-9").text
    print(driver.window_handles)#for debug
    #try:#open a new tab
        #driver.find_element_by_css_selector(".col-md-9").click()
    #finally:
        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    return data

items=['HLJ', 'JL', 'LN', 'BJ', 'TJ', 'NMG', 'HB', 'SX', 'SAX', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97 %E4%B8%8A%E6%B5%B7'] #'%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7','
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
output=[]
chromedriver ='C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
print('here we go chrome')
driver = webdriver.Chrome(chromedriver)
driver.get('http://qichacha.com/user_login')
for i in range(20):
    print('time.sleep',20-i)
    time.sleep(1)

import re #(pre-treatment)
print('url=',url)
for item in items:
    for company in companies:
        i=1
        while True:
            text=chrome(url.format(company,item,i))
            time.sleep(2.98)
            try:
                re.search('善林',text).group(0)
            except AttributeError:
                print('Page=',i,'\nitem=',item,'\ncompany=',company,'\ntext=',text,'\n',AttributeError)#for break
                break
            else:
                output.append(re.findall('善林.*? 存续|善林.*? 在业',text))
                print(item,company,i,output[-1])
            finally:
                i=i+1
print(output)
#elem = driver.find_element_by_link_text(nextpage)
#elem.click()
fileObj.write(str(output))
fileObj.close()
driver.close()
driver.quit()
