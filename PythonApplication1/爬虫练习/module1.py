from urllib import request
#easy response
response = request.urlopen("http://www.baidu.com/")
content = response.read()
print(content)

import bs4