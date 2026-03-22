# coding = utf-8

from selenium import webdriver

import os
import time   #调入time函数

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
time.sleep(0.3)  #休眠0.3秒
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)  # 休眠3秒
print(driver.title)  # 把页面title 打印出来

browser.quit()
