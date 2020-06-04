# 读取数据
filePath=r'F:\\OneDrive\\华莱士\\Documents\\门店监控项目\\城市-营运-督导-门店.csv'

from flask import Flask

# 时间
import datetime

import pandas,numpy
numpy.random.seed(None)
fl = pandas.read_csv(filePath,encoding='gbk').astype('str').sample(frac=1,random_state=numpy.random.RandomState())
fl.drop_duplicates(subset=['城市经理'],keep='first',inplace=True)## 自动去重，确保每个【城市经理】只命中一次

# 网页服务器部分：
###网页模版
template1='''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"><html xmlns="http://www.w3.org/1999/xhtml"><body><a href="../chou/30"><button type="button" class="btn btn-warning">点此按钮随机抽30个</button></a><div class="container">'''
template2='''</div><link href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" media="screen"><script src="http://apps.bdimg.com/libs/jquery/2.0.0/jquery.min.js"></script><script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script></body></html>'''

###初始化程序_定义服务器
global app
app = Flask(__name__)

@app.route('/chou/<n>', methods=("GET", "POST"))
def 入魂(n):    return template1 + "当前时间：" + datetime.datetime.now().strftime("%x %X") + 一发入魂(n=int(n)).to_html(classes='table-striped') + template2

# @app.route('/city/<city>/<n>', methods=("GET", "POST"))
# def by区域(city,n=None):    return template1 + "当前时间：" +  datetime.datetime.now().strftime("%x %X") + 按区域抽(区域=city,n=int(n) if n else None).to_html(classes='table-striped') + template2

@app.route('/', methods=("GET", "POST"))
def index():return template1 + "当前时间：" + datetime.datetime.now().strftime("%x %X") +  template2

# 抽签开始
def 一发入魂(n=None, frac=None, replace=False):    return fl.sample(n=n,frac=frac,replace=replace)
def 抽个区域(n=None, frac=None, replace=False):    return fl['区域'].sample(n=n,frac=frac,replace=replace)
def 按区域抽(区域,n=None, frac=None, replace=False):    return fl[fl['区域']==区域].sample(n=n,frac=frac,replace=replace)
def 按城市经理抽(城市经理,n=None, frac=None, replace=False):    return fl[fl['城市经理']==城市经理].sample(n=n,frac=frac,replace=replace)
def 按督导抽(督导,n=None, frac=None, replace=False):    return fl[fl['督导']==督导].sample(n=n,frac=frac,replace=replace)

# 直接选
def 选个区域():    return fl['区域'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())
def 选个城市经理(区域):    return fl[fl['区域']==区域]['城市经理'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())
def 选个督导(城市经理):    return fl[fl['城市经理']==城市经理]['督导'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())

#测试随机抽取用
if __name__=='__main__':
    print(
    "按区域抽(区域='上海')",按区域抽(区域='上海'),
    "按城市经理抽(城市经理='蔡欢')",按城市经理抽(城市经理='蔡欢'),   
    "选个区域()",选个区域(),
    "选个城市经理(区域='福州')",选个城市经理(区域='福州'),
    "选个督导(城市经理='蔡欢')",选个督导(城市经理='蔡欢'),
    )
#     "按督导抽(督导='刘立福')",按督导抽(督导='王冰'), 

###启动主程序——网页服务器
if __name__ == '__main__':
    print('启动主程序——网页服务器',datetime.datetime.now().strftime("%x %X"))
    app.run()
    #结束程序
    print('Thank you',datetime.datetime.now().strftime("%x %X"))