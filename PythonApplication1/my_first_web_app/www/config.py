# -*- coding: utf-8 -*-
'''
setting.

# Flask development cfg
# Website
# config.cfg
'''

__author__ = 'lai yao (lake.lai)'
	
#Flask
HOST = 'localhost'
PORT = 5000
DEBUG = True
SECRET_KEY = 'development key'

#toolbar = DebugToolbarExtension(app),http://www.pythondoc.com/flask-debugtoolbar/index.html
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS =True
DEBUG_TB_PROFILER_ENABLED = False
DEBUG_TB_TEMPLATE_EDITOR_ENABLED = False

#Website set
info={
'Title':'Yao',
'WebPage':'Page',
'WebName':'MyFirstWebPython'
}