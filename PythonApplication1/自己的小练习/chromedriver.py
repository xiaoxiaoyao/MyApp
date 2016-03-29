# -*- coding: utf-8 -*-
import os
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
items=['HLJ', 'JL', 'LN', 'BJ', 'TJ', 'NMG', 'HB', 'SX', 'SAX', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E9%87%91%E8%9E%8D%E4%BF%A1%E6%81%AF%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8','%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8']
#companies=['善林（上海）商务咨询有限公司', '善林（上海）金融信息服务有限公司', '善林（上海）信息科技有限公司', '善林（上海）商务咨询服务有限公司']
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
chromedriver ='C:\\Users\\yaopr\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
for item in items:
    for company in companies:
        for i in range(19):
            driver.get(url.format(company,item,i))
            time.sleep(3)  # 休眠3秒

#assert "善林（上海）金融信息服务有限公司" in driver.title
#elem = driver.find_element_by_link_text(nextpage)
#elem.click()

driver.close()
driver.quit()