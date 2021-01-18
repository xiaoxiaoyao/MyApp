
# 读取数据，上传服务器时，请修改此行为对应的文件位置
filePath=r'F:\\OneDrive\\华莱士\\Documents\\门店监控项目\\市场组织架构收集\\城市-营运-督导-门店.csv'

from flask import Flask

# 时间
import datetime

import pandas,numpy.random
numpy.random.seed(int(datetime.datetime.now().strftime("%j")))
fl = pandas.read_csv(filePath).astype('str').sample(frac=1,random_state=numpy.random.RandomState())
fl['label'] = '0'
# fl.drop_duplicates(subset=['城市经理'],keep='first',inplace=True)## 自动去重，确保每个【城市经理】只命中一次

# 网页服务器部分：
###网页模版
template1='''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"><html xmlns="http://www.w3.org/1999/xhtml"><body><a href="../chou/30"><button type="button" class="btn btn-warning">点此按钮随机抽30个</button></a><a href="../all"><button type="button" class="btn btn-warning">点此按钮一键全抽</button></a><a href="../all-no-repeat"><button type="button" class="btn btn-warning">不重复全抽城市经理</button></a>
<a href="../3-suzhou-1-shanghai"><button type="button" class="btn btn-warning">按：苏州30上海10抽取</button></a>
<br /><div class="container">'''
template2='''</div><link href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" media="screen"><script src="http://apps.bdimg.com/libs/jquery/2.0.0/jquery.min.js"></script><script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script></body></html>'''

###初始化程序_定义服务器
global app
app = Flask(__name__)

@app.route('/chou/<n>', methods=("GET", "POST"))
def 入魂(n):    return template1 + "当前时间：" + datetime.datetime.now().strftime("%x %X") + 一发入魂(n=int(n)).to_html(classes='table-striped') + template2
    
@app.route('/all', methods=("GET", "POST")) #一键全抽城市经理(不去重)
def 一键全抽城市经理():    return template1 + "当前时间：" + datetime.datetime.now().strftime("%x %X") + 城市经理一键全抽().to_html(classes='table-striped') + template2

@app.route('/all-no-repeat/reset', methods=("GET", "POST")) #一键全抽城市经理
def all_no_repeat_reset(): 
    fl['label'] = '0'
    return  template1 +'重置抽取计数器成功' + template2

@app.route('/all-no-repeat', methods=("GET", "POST")) #一键全抽城市经理
def 不重复抽城市经理():    return template1 + '<a href="../all-no-repeat/reset"><button type="button" class="btn btn-warning">重置抽取计数器</button></a>'+ "今天是全年的第" + datetime.datetime.now().strftime("%j") + "天，服务器当前时间：" + datetime.datetime.now().strftime("%x %X") + 城市经理不重复抽().to_html(classes='table-striped') + template2

# 临时功能，抽10个上海，30个苏州(不去重)
@app.route('/3-suzhou-1-shanghai', methods=("GET", "POST"))
def by区域():    return template1 + "当前时间：" +  datetime.datetime.now().strftime("%x %X") + 按区域抽(区域='江苏苏州服务区',n=30).to_html(classes='table-striped')  + 按区域抽(区域='上海',n=10).to_html(classes='table-dark') + template2

# 首页
@app.route('/', methods=("GET", "POST"))
def index():    return template1 + "当前时间：" + datetime.datetime.now().strftime("%x %X") +  template2

# 抽签开始
# 中间的.drop_duplicates(subset=['城市经理'],keep='first')是用来保证一个'城市经理'只被抽中一次的
def 一发入魂(fl=fl,n=None, frac=None, replace=False):    return fl.sample(n=n,frac=frac,replace=replace).drop_duplicates(subset=['城市经理'],keep='first')
def 抽个区域(fl=fl,n=None, frac=None, replace=False):    return fl['区域'].sample(n=n,frac=frac,replace=replace).drop_duplicates(subset=['城市经理'],keep='first')
def 按区域抽(区域,fl=fl,n=None, frac=None, replace=False):    return fl[fl['区域']==区域].sample(n=n,frac=frac,replace=replace)# 不去重
def 按城市经理抽(城市经理,fl=fl,n=None, frac=None, replace=False):    return fl[fl['城市经理']==城市经理].sample(n=n,frac=frac,replace=replace).drop_duplicates(subset=['城市经理'],keep='first')
def 按督导抽(督导,n=None, fl=fl,frac=None, replace=False):    return fl[fl['督导']==督导].sample(n=n,frac=frac,replace=replace).drop_duplicates(subset=['城市经理'],keep='first')
def 城市经理一键全抽(fl=fl):    return fl.sample(frac=1,random_state=numpy.random.RandomState()).drop_duplicates(subset=['城市经理'],keep='first')

#不重复抽取（重构一下）
def 城市经理不重复抽():
    tmp=fl[fl.label=='0'].sample(frac=1,random_state=numpy.random.RandomState()).drop_duplicates(subset=['城市经理'],keep='first')
    fl.loc[tmp.index,'label']= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return tmp

# 直接选
def 选个区域():    return fl['区域'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())
def 选个城市经理(区域):    return fl[fl['区域']==区域]['城市经理'].sample(frac=1,random_state=numpy.random.RandomState()).drop_duplicates()
def 选个督导(城市经理):    return fl[fl['城市经理']==城市经理]['督导'].sample(frac=1,random_state=numpy.random.RandomState()).drop_duplicates()

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
    app.run() # 上传服务器时请输入正确的端口（参考之前的文件同位置内容）
    #结束程序
    print('Thank you',datetime.datetime.now().strftime("%x %X"))
