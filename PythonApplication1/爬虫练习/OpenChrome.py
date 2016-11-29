# -*- coding: utf-8 -*-
'''
打开Chrome

开启Chrome时直接复制粘贴这段代码即可
'''
__author__ = 'lai yao (lake.lai)'
URL='https://chromedriver.storage.googleapis.com/index.html?'

def start():
	##/初始化路径
	import os,sys,time
	try:
		path = os.path.abspath(os.path.dirname(sys.argv[0]))
		fileObj = open(path + '\\output.txt','w') 
		fileObj2 = open(path + '\\test.txt','w') 
	except FileNotFoundError as err:
		path = 'F:\\Documents\\Visual Studio 2015\\Projects\\PythonApplication1\\PythonApplication1\\爬虫练习'
		fileObj=[]
		fileObj2=[]
		pass
	except BaseException as err:
		path = 'F:\\Documents\\Visual Studio 2015\\Projects\\PythonApplication1\\PythonApplication1\\爬虫练习'
		fileObj=[]
		fileObj2=[]
		pass
	finally:
		fileObj = open(path + '\\output.txt','w') 
		fileObj2 = open(path + '\\test.txt','w') 
		print(path)
		chromedriver =path + '\\chromedriver.exe'
	
	##引入selenium，设置Chrome
	from selenium import webdriver
	import selenium
	os.environ["webdriver.chrome.driver"] = chromedriver
	option = webdriver.ChromeOptions()#自定义设置
	option.add_argument('--user-data-dir=' + os.getenv('APPDATA') + '\\..\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录##注意退出当前的chrome
	##option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1') #修改浏览器的User-Agent来伪装你的浏览器
	option.add_argument('--process-per-site') #每个站点使用单独进程
	option.add_argument('--lang=zh-CN') #设置语言为简体中文

	##启动浏览器
	driver = webdriver.Chrome(chromedriver,chrome_options=option)
	driver.get('about:version')
	return driver

if __name__  ==  '__main__' :
	Driver=start()