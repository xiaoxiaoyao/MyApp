import requests,random,time
import leancloud
appid=input("https://console.qcloud.com/tab:{{appid}}")
appkey=input("{{appkey}}")
leancloud.init(appid,appkey)

from leancloud import Object,LeanCloudError,Query

headers={'Host':'www.bugbank.cn',
'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:47.0)Gecko/20100101Firefox/47.0',
'Accept':'application/json,text/javascript,*/*;q=0.01',
'Accept-Language':'en-US,zh;q=0.8,zh-CN;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip,deflate',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
'x-client-id':'user-web',
'X-Requested-With':'XMLHttpRequest',
'Referer':'http://www.bugbank.cn/signup.html',
'Content-Length':'197',
'Connection':'keep-alive'}
url='http://www.bugbank.cn/api/signup'
code='%016d' % random.randint(0,1000000000000000)
data={'name':'xiaoxiaoyao','email':'yao.power@qq.com','password':code,'code':code}

#//使用云存储你们说吼不吼啊
TestObject= Object.extend('TestObject')
test_object = TestObject()
test_object.set('headers', headers)
test_object.set('url', url)

def post(code):
	data={'name':'xiaoxiaoyao','email':'yao.power@qq.com','password':code + code,'code':code}
	res1 = requests.post(url, data=data, headers=headers)
	return res1
def loop():
        code='%016d' % random.randint(0,10000000000000000)
        j=post(code)
        i=j.status_code
        print(time.asctime() ,i)
        time.sleep(10)
        try:
            test_object.save()
        except LeanCloudError:
            print(LeanCloudError)
        if (i == 406) or (i == 409) or (i == 429) or (i == 504):
                output='post(code) == 406失效邀请码/409/429/504'+code
                print(output)
                test_object.set(code, output)
                return 0
        else:
                output=time.asctime() + 'NOT post(code) == 406/409/429 AND code='+j.content,code
                print(output)
                test_object.set(code, output)
                return 1

def run():
        while True:
                try:
                        i=loop()
                        print('\n')
                finally:
                        if i==1:
                                break

if __name__ == '__main__':
        run()
                
	
