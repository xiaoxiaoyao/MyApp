# -*- coding: utf-8 -*-
'''
我的第一个爬虫

爬自己公司的所有子公司，方便搜索，简单粗暴
'''
__author__ = 'lai yao (lake.lai)'

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
from selenium import webdriver
import selenium
#from selenium.webdriver.common.keys import Keys

##import asyncio
##loop = asyncio.get_event_loop()
def quit():
    fileObj.close()
    fileObj2.close()
    driver.quit()
    i=-1#for quit
    logging.info(['QUIT success'])
    return

def closelastpage(dri,i=1):
    if len(dri.window_handles)<=1:
        return  #页面开了没？
    dri.switch_to_window(dri.window_handles[len(dri.window_handles)-1])#切换到最后一个标签页
    dri.close()
    pass
  
def chrome(url):
    logging.info(['def chrome(url):'])
    driver.get(url)
    data=[]
    j=1
    while True:
        try:
            driver.switch_to_window(window_handles0)
            data.append(driver.find_element_by_xpath(str('//*[@id="searchlist"]['+str(j)+']')).text)
            fileObj2.write(data[-1])
            driver.switch_to_window(window_handles0)
        except selenium.common.exceptions.NoSuchElementException as err:
            logging.info([j,err])
            return str(data)
            break
        except BaseException as err:
           logging.info([j,err])
           logging.info(['BaseException??? in def chrome(url,j=1):'])
           return
        else:
            logging.info([j,'(found)',data[j-1]])
            qichacha_update(driver,j)#顺带更新一下数据
            ##loop.run_until_complete(qichacha_update(driver,j))
        finally:
            driver.switch_to_window(window_handles0)
            j=j+1
            pass

def qichacha_update(dri=None,i=1):
    logging.info(['def qichacha_update(dri=',dri,',i=',i,'):'])
    logging.info([dri.window_handles,'dri.switch_to_window(dri.window_handles[',len(dri.window_handles)-1,']'])#for debug
    time.sleep(1)
    #顺带更新一下数据
    dri.find_element_by_xpath(str('//*[@id="searchlist"]['+str(i)+']')).click()
    time.sleep(1)
    if len(dri.window_handles)<=1:
        return  #页面开了没？
    dri.switch_to_window(dri.window_handles[len(dri.window_handles)-1])
    time.sleep(1)
    try:
        dri.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/a[3]').click()
        time.sleep(1)
        dri.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/a[1]').click()
        dri.switch_to_window(window_handles0)
    except selenium.common.exceptions.NoSuchElementException as err:
        logging.info([i,err])
        logging.info(['no found update date 哎呀没点到更新数据'])
        return
    except BaseException as err:
        logging.info([i,err])
        logging.info(['BaseException??? in def qichacha_update(dri=None,i=1):'])
        return
    else:
        time.sleep(1)
        dri.switch_to_window(dri.window_handles[len(dri.window_handles)-1])#切换到最后一个标签页
        dri.close()
    finally:
        dri.switch_to_window(window_handles0)
        logging.info([dri.window_handles,'finally:dri.switch_to_window(dri.window_handles[0])#for debug'])
    pass

##初始化##
##初始化调试日志
import logging 
logging.basicConfig(
    level=logging.INFO, #日志级别，默认为logging.WARNING,日志级别的关系为：CRITICAL》ERROR》WARNING》INFO》DEBUG》NOTEST
    #format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
    #datefmt='%a, %d %b %Y %H:%M:%S', #指定时间格式
    filename='chromedriver.log', #日志文件名，没有会自动生成
    filemode='w'  #覆盖之前log
)
items=['SX', 'NMG', 'HB', 'SAX', 'HLJ', 'JL', 'LN', 'BJ', 'TJ', 'QH', 'GS', 'NX', 'XJ', 'SH', 'JS', 'ZJ', 'AH', 'FJ', 'JX', 'SD', 'GD', 'GX', 'HAIN', 'HEN', 'HUB', 'HUN', 'CQ', 'SC', 'GZ', 'YN', 'XZ']
companies=['%E5%96%84%E6%9E%97 %E4%B8%8A%E6%B5%B7'] #'%E5%96%84%E6%9E%97%EF%BC%88%E4%B8%8A%E6%B5%B7','
url='http://qichacha.com/search?key={0}&province={1}&p={2}&index='
output=[]
chromedriver =path + '\\chromedriver.exe'
logging.info([chromedriver])
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()#自定义设置
option.add_argument('--user-data-dir=' + os.getenv('APPDATA') + '\\..\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录##注意退出当前的chrome
option.add_argument('--user-agent=Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1') #修改浏览器的User-Agent来伪装你的浏览器
option.add_argument('--process-per-site') #每个站点使用单独进程
option.add_argument('--lang=zh-CN') #设置语言为简体中文
##完成初始化##
driver = webdriver.Chrome(chromedriver,chrome_options=option)
driver.get('about:version')
time.sleep(2)
logging.info(['##完成初始化##成功开启chrome##'])
driver.get('http://qichacha.com/user_login')
time.sleep(1)

import re #(pre-treatment)
logging.info(['url=',url])
i=1
company=companies[0]
for item in items:
    while i != -1:
        logging.info(['\n\ntext=chrome(url.format(company,item,i)) url.format(company,item,i)=',url.format(company,item,i)])
        try:
            window_handles0=driver.window_handles[0]
            logging.info(window_handles0)
            text=chrome(url.format(company,item,i))
            time.sleep(1)
            re.search('善林',text).group(0)
        except AttributeError:
            logging.info(['Page=',i,'\nitem=',item,'\ncompany=',company,'\ntext=',text,'\n',AttributeError,'#for break'])
            i=1
            break
        except KeyboardInterrupt:
            logging.info(['KeyboardInterrupt',KeyboardInterrupt])
            quit()
            break
        except ConnectionResetError as err:
            logging.info(['e,页面被关了，退出吧',err])
            quit()
            #driver.get('about:version')#要不重新开？
            pass
            break
        except BaseException as err:
            logging.info(['except BaseException as err:',err,'/nBaseException??? in for item in items: while i != -1:'])
            quit()
            break
        else:
            output.append(re.findall('善林.*? 存续|善林.*? 在业',text))
            fileObj.write(str(output[-1]))
            fileObj.write('\n')
            logging.info([item,company,i,driver.current_url,output[-1]])
            i=i+1
        finally:
            logging.info(['try-finally : Page=',i,'item=',item,'company=',company,'\n'])
logging.info([output])
#elem = driver.find_element_by_link_text(nextpage)
#elem.click()
#fileObj.write(str(output))
fileObj.close()
fileObj2.close()
driver.close()
driver.quit()