import pandas,numpy
from flask import Flask, render_template

numpy.random.seed(None)
fl = pandas.read_csv(r'F:\\OneDrive\\华莱士\\Documents\\门店监控项目\\城市-营运-督导-门店.csv',encoding='gbk').astype('str')

def 一发入魂(n=None, frac=None, replace=False):
    return fl.sample(n=n,frac=frac,replace=replace)

# 抽签开始

def 抽个区域(n=None, frac=None, replace=False):
    return fl['区域'].sample(n=n,frac=frac,replace=replace)

def 按区域抽(区域,n=None, frac=None, replace=False):
    return fl[fl['区域']==区域].sample(n=n,frac=frac,replace=replace)

def 按城市经理抽(城市经理,n=None, frac=None, replace=False):
    return fl[fl['城市经理']==城市经理].sample(n=n,frac=frac,replace=replace)

def 按督导抽(督导,n=None, frac=None, replace=False):
    return fl[fl['督导']==督导].sample(n=n,frac=frac,replace=replace)

# 直接选

def 选个区域():
    return fl['区域'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())

def 选个城市经理(区域):
    return fl[fl['区域']==区域]['城市经理'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())

def 选个督导(城市经理):
    return fl[fl['城市经理']==城市经理]['督导'].drop_duplicates().sample(frac=1,random_state=numpy.random.RandomState())

if __name__=='__main__':
    print(
    "按区域抽(区域='上海')",按区域抽(区域='上海'),
    "按城市经理抽(城市经理='蔡欢')",按城市经理抽(城市经理='蔡欢'),
    "按督导抽(督导='刘立福')",按督导抽(督导='刘立福'),
    "选个区域()",选个区域(),
    "选个城市经理(区域='福州')",选个城市经理(区域='福州'),
    "选个督导(城市经理='蔡欢')",选个督导(城市经理='蔡欢'),
    )
