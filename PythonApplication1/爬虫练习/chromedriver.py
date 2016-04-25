# -*- coding: utf-8 -*-
'''
我的第一个爬虫

爬自己公司的所有子公司，方便搜索，简单粗暴
'''
__author__ = 'lai yao (lake.lai)'

import os,time
fileObj = open('C:\\Users\\yaopr\\Source\\Repos\\PythonApplication1\\OUTPUT\\output.txt','w') 
fileObj2 = open('C:\\Users\\yaopr\\Source\\Repos\\PythonApplication1\\OUTPUT\\test.txt','w') 
from selenium import webdriver

#from selenium.webdriver.common.keys import Keys

##import asyncio
##loop = asyncio.get_event_loop()

def chrome(url):
    print('def chrome(url):')
    driver.get(url)
    data=[]
    i=1
    while True:
        try:
            driver.switch_to_window(driver.window_handles[0])
            data.append(driver.find_element_by_xpath(str('//*[@id="searchlist"]['+str(i)+']')).text)
            fileObj2.write(data[-1])
            driver.switch_to_window(driver.window_handles[0])
        except BaseException as err:
            print(i,err)
            return str(data)
            break
        else:
            print(i,'(found)',data[i-1])
            qichacha_update(driver,i)#顺带更新一下数据
            ##loop.run_until_complete(qichacha_update(driver,i))
            i=i+1
        finally:
            pass

def qichacha_update(dri=None,i=1):
    print('def qichacha_update(dri=',dri,',i=',i,'):')
    print(dri.window_handles,'dri.switch_to_window(dri.window_handles[',len(dri.window_handles)-1,'])')#for debug
    time.sleep(1)
    #顺带更新一下数据
    dri.find_element_by_xpath(str('//*[@id="searchlist"]['+str(i)+']')).click()
    time.sleep(1)
    if len(dri.window_handles)<=1:
        return  #页面开了没？
    dri.switch_to_window(dri.window_handles[len(dri.window_handles)-1])
    time.sleep(3)
    dri.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/a[3]').click()
    time.sleep(1)
    dri.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/a[3]/i').click()
    dri.switch_to_window(dri.window_handles[0])
    time.sleep(7)
    dri.switch_to_window(dri.window_handles[len(dri.window_handles)-1])#切换到最后一个标签页
    dri.close()
    dri.switch_to_window(dri.window_handles[0])
    print(dri.window_handles,'dri.switch_to_window(dri.window_handles[0])')#for debug
    pass


items=['HLJ', 'JL', 'LN', 'BJ', 'TJ', 'NMG', 'HB', 'SX', 'SAX', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97 %E4%B8%8A%E6%B5%B7'] #'%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7','
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
output=[]
chromedriver ='C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()#自定义设置
option.add_argument('--user-data-dir=C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录##注意退出当前的chrome
option.add_argument('--user-agent=iphone') #修改浏览器的User-Agent来伪装你的浏览器访问手机m站
option.add_argument('--process-per-site') #每个站点使用单独进程
option.add_argument('--lang=zh-CN') #设置语言为简体中文
print('here we go chrome')
driver = webdriver.Chrome(chromedriver,chrome_options=option)
driver.get('about:version')
time.sleep(1)
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
                fileObj.write(str(output[-1]))
                print(item,company,i,driver.current_url,output[-1])
            finally:
                i=i+1
print(output)
#elem = driver.find_element_by_link_text(nextpage)
#elem.click()
#fileObj.write(str(output))
fileObj.close()
fileObj2.close()
driver.close()
driver.quit()
