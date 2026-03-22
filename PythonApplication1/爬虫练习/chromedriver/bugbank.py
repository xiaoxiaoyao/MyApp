import requests,random,time
import leancloud
appid="cUU6wIhChQVnpXDizDcU5QP6-9Nh9j0Va"
appkey="1EPMbPARtaHFPvvcQTWyBP2G"#//AppKey 是客户端中使用的 Key，理论上客户端中所有请求都不应被信任，默认应认为 AppKey 是泄露的
#//防御恶意请求，不应通过加密 App Key，而应通过设置 ACL（访问权限控制列表）来实现，详细请参考 「数据与安全文档」
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
test_object.destroy()
test_object.save()
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
		except LeanCloudError as err:
				print(err)
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
				except KeyboardInterrupt as err:
						print(err)
						break
				finally:
						if i==1:
								break
				print(test_object.fetch())
if __name__ == '__main__':
		run()
		test_object.destroy()
		test_object.save()
