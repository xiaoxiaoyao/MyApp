# -*- coding: utf-8 -*-
'''
智联招聘，帮我投简历

注意修改一下#搜索职位关键词 的值,timeout为超时等待时间，根据网络情况设定
'''
if __name__=='__main__':
	timeout=10
	KeyWordUrl='http://sou.zhaopin.com/jobs/searchresult.ashx?kw=%E7%A8%8E&sm=0&bj=2060000&isfilter=1&p=1&sf=8001&st=8000'
	#KeyWordUrl='http://sou.zhaopin.com/jobs/searchresult.ashx?kw=%E7%A8%8E&sm=0&bj=2060000&isfilter=1&p=1&sf=8001&st=10000'
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
	#别自定义设置了吧
	#option = webdriver.ChromeOptions()#自定义设置
	#option.add_argument('--user-data-dir=' + os.getenv('APPDATA') + '\\..\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录##注意退出当前的chrome
	###option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1') #修改浏览器的User-Agent来伪装你的浏览器
	#option.add_argument('--process-per-site') #每个站点使用单独进程
	#option.add_argument('--lang=zh-CN') #设置语言为简体中文

	##启动浏览器
	#driver = webdriver.Chrome(chromedriver,chrome_options=option)
	driver = webdriver.Chrome(chromedriver)
	driver.get('http://www.zhaopin.com/?about:version')
	time.sleep(1)
	n=driver.find_element_by_xpath('//*[@id="loginname"]')
	n.send_keys("13681776437")
	print('#给你60秒输入用户名密码你懂得')#给你输入用户名密码你懂得
	for n in range(60):
		time.sleep(1)
		print(n+1,'秒')
	driver.get(KeyWordUrl)#搜索职位关键词
	driver.switch_to_window(driver.window_handles[len(driver.window_handles)-1])#切换到最后一个标签页
	for n in range(25):
		print(n,'for n in range(25):')
		time.sleep(timeout)
		try:
			driver.find_element_by_xpath('//*[@id="newlist_list_content_table"]/table['+ str(n+2) + ']/tbody/tr[1]/td[1]/div/a').click()
			time.sleep(timeout)
			driver.switch_to_window(driver.window_handles[len(driver.window_handles)-1])#切换到最后一个标签页
			driver.find_element_by_xpath('//*[@id="applyVacButton1"]').click()
			time.sleep(timeout)
			driver.switch_to_window(driver.window_handles[len(driver.window_handles)-1])#切换到最后一个标签页
			driver.find_element_by_xpath('//*[@id="list_d"]/div[1]/div[1]/button[1]').click()
			time.sleep(timeout)
		except BaseException as err:
			print(err)
			driver.get(KeyWordUrl)#搜索职位关键词
			driver.switch_to_window(driver.window_handles[0])#切换到第一个标签页
			driver.get(KeyWordUrl)#搜索职位关键词
		else:
			driver.close()
		finally:
			driver.switch_to_window(driver.window_handles[0])#切换到第一个标签页
	driver.close()
	driver.quit()
