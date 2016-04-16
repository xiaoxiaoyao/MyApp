# -*- coding: utf-8 -*-
'''
我的第一个爬虫

爬自己公司的所有子公司，方便搜索，简单粗暴
'''
__author__ = 'lai yao (lake.lai)'

import os,time
fileObj = open('C:\\Users\\yaopr\\Source\\Repos\\PythonApplication1\\OUTPUT\\output.txt','w') 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##import asyncio
##loop = asyncio.get_event_loop()

def chrome(url):
    print('def chrome(url):')
    driver.get(url)
    data=[]
    i=1
    while True:
        try:
            ##driver.switch_to_window(driver.window_handles[0])
            data.append(driver.find_element_by_xpath(str('//*[@id="searchlist"]['+str(i)+']')).text)
            ##loop.run_until_complete(qichacha_update(driver,i))
            ##driver.switch_to_window(driver.window_handles[0])
        except BaseException as err:
            print(i,err)
            return str(data)
            break
        else:
            print(i,'(found)',data[i-1])
            i=i+1

##async def qichacha_update(driver=None,i=1):
##    print('def qichacha_update(driver=None,i=1):')
##    print(driver.window_handles)#for debug
##    await asyncio.sleep(1)
##    #顺带更新一下数据
##    driver.find_element_by_xpath(str('//*[@id="searchlist"]['+str(i)+']')).click()
##    driver.switch_to_window(driver.window_handles[1])
##    driver.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/a[3]').click()
##    driver.switch_to_window(driver.window_handles[0])
##    await asyncio.sleep(1)
##    driver.switch_to_window(driver.window_handles[1])
##    driver.close()
##    driver.switch_to_window(driver.window_handles[0])
##    pass


items=['HLJ', 'JL', 'LN', 'BJ', 'TJ', 'NMG', 'HB', 'SX', 'SAX', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97 %E4%B8%8A%E6%B5%B7'] #'%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7','
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
output=[]
chromedriver ='C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
print('here we go chrome')
driver = webdriver.Chrome(chromedriver)
driver.get('http://qichacha.com/user_login')
for i in range(10):
    print('time.sleep',10-i)
    time.sleep(1)

import re #(pre-treatment)
print('url=',url)
for item in items:
    for company in companies:
        i=1
        while True:
            print('\n\n\n\n\n\ntext=chrome(url.format(company,item,i))')
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
