# -*- coding: utf-8 -*-
# Flask development cfg
# config.cfg
'''
#Flask里面是Flask的设置内容，部署的时候记得把DEBUG改成 False
#Website里面info是网站基础设置
'''

#Flask
HOST = 'localhost'
PORT = 5000
DEBUG = True
SECRET_KEY = 'development key'

#Website
info={
'Title':'Yao',
'WebPage':'Page',
'WebName':'MyFirstWebPython'
}