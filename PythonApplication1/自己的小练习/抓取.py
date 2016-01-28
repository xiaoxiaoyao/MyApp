#最基本的抓站，两句话就可以了.使用requests来加载一个 web 页面是非常简单的：

import requests
response = requests.get('http://www.britishchambershanghai.org/en/directory/list?page=6')

#解析网站
import bs4
soup = bs4.BeautifulSoup(response.text)
links = soup.select('div.info-container a[href^=/en/directory/]')

