from urllib import request
#最基本的抓站
response = request.urlopen("http://www.baidu.com/")
content = response.read()
print(content)