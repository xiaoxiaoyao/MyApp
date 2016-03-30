# -*- coding: utf-8 -*-

import os
fileObj = open('C:\\Users\\yaopr\\AppData\\Local\\Temp\\adcon\\output.txt','w') 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def chrome(url):
    driver.get(url)
    data=driver.find_element_by_class_name("col-md-9").text
    return data

items=['HLJ', 'JL', 'LN', 'BJ', 'TJ', 'NMG', 'HB', 'SX', 'SAX', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E9%87%91%E8%9E%8D%E4%BF%A1%E6%81%AF%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
output=[]
chromedriver ='C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://qichacha.com/user_login')
for i in range(20):
    print('time.sleep',20-i)
    time.sleep(1)
for item in items:
    for company in companies:
        for i in range(9):
            output.append([item,company,url,chrome(url.format(company,item,i))])
            print(output[-1])
            time.sleep(2.98) 
print(output)
#elem = driver.find_element_by_link_text(nextpage)
#elem.click()
fileObj.write(output)
fileObj.close()
driver.close()
driver.quit()
