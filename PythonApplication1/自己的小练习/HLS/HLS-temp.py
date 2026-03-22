#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd 
import numpy as np 
import sys


file_path=r"F:\OneDrive\华莱士\电商\电商\\"
file_name="\测试数据.xlsx"


def run_code(file_name):
    file=file_path+file_name
    df = pd.read_excel(file,
                    usecols = "D,M,R:AD",
                    sheet_name= '订单明细')
    df.head(10)


    # In[35]:


    # 设定保底和费率
    设定保底=4.5
    设定费率=15

    # 测算保底和费率
    测算保底=0 # 这个没保底的
    测算费率=20

    print(
    """
    配送方式	费率	保底
    美团快送	15.0%	4.5
    美团专送	15.0%	4.5
    到店取餐	5.0%	0.5
    津贴联盟		-
    代理商配送	16.0%	-按原价
    商家自配	16.0%	-
    只测算美团的
    """)

    df.dtypes


    # In[36]:


    # 版本0.21.0引入了infer_objects()方法，用于将具有对象数据类型的DataFrame的列转换为更具体的类型。

    df['美团活动补贴']=df['美团活动补贴'].replace('-',0).astype(float)
    df['用户支付配送费']=df['用户支付配送费'].replace('-',0).astype(float)
    df['用户线上支付金额']=df['用户线上支付金额'].replace('-',0).astype(float)
    try:
        df['费率']=df['费率'].str.strip("%").astype(float) # Python如何将百分号的字符转成数字
    except AttributeError as err:
        print(err)

    df['保底']=df['保底'].replace('-',0).astype(float) # Python强行转换格式

    df美团待测算=df

    df美团待测算.dtypes


    # In[37]:


    print("当前最大费率（代理商费率16，美团专送15）：",df['费率'].max(),"当前最大保底：",df['保底'].max())
    print("""
    费率	计数
    """,df美团待测算['费率'].value_counts())


    # In[38]:


    print("描述性统计，数据收集目标：保底订单计数，总订单计数，全部客单价、保底客单价、抽点客单价（筛选美团外卖）")

    df美团待测算.loc[df美团待测算['平台服务费']== -df美团待测算['保底'],'是否保底']=True # 算保底
    df美团待测算['是否保底']=df美团待测算['是否保底'].fillna(False)
    df美团待测算.head(10)


    # In[39]:


    df描述性统计1=df美团待测算.groupby(['交易类型','配送方式','是否保底'])['平台服务费','用户线上支付金额','用户支付配送费','美团活动补贴'].count().reset_index()
    df描述性统计1['统计']='计数'
    df描述性统计1['文件名']=file_name


    # In[40]:


    df描述性统计2=df美团待测算.groupby(['交易类型','配送方式','是否保底'])['平台服务费','用户线上支付金额','用户支付配送费','美团活动补贴'].mean().reset_index()
    df描述性统计2['统计']='平均值'
    df描述性统计2['文件名']=file_name


    # In[41]:


    df描述性统计3=df美团待测算.groupby(['交易类型','配送方式','是否保底'])['平台服务费','用户线上支付金额','用户支付配送费','美团活动补贴'].sum().reset_index()
    df描述性统计3['统计']='求和'
    df描述性统计3['文件名']=file_name

    pd.concat([df描述性统计1,df描述性统计2,df描述性统计3],axis=0).to_csv(file_path +  '输出汇总-河北' + '.csv', encoding='utf_8_sig', mode='a', header=False)

    pass


file_name=[
r"河北.xls"
]

for i in file_name:
    print(i,"reading")
    try:
        run_code(i)
    except BaseException as err:
        print(err)
    print(i,"OK")
