# 1. 首先将要使用的库全部进行导入，并设置程序运行路径

import os
os.chdir(r"F:\OneDrive\华莱士\Documents\office培训\PYTHON培训\第四周")
#设置路径
import pandas as pd
import matplotlib.pyplot as plt
#处理数据及绘图
import warnings
warnings.filterwarnings('ignore')
#忽略警报
from bokeh.io import output_file
from bokeh.plotting import figure,show
from bokeh.models import ColumnDataSource
#交互式处理

# 2. 数据导入并查看数据

df = pd.read_csv("上海餐饮数据.csv")
print(df.head(15)) # 查看前15条数据

# 进行数据量以及标题信息的查看

print(df.columns.tolist())
print('总数据量为{}条'.format(len(df)))

# 3. 不同类别评价指标的选择

# 通过表格输出可以发现，对于不同的菜系类别，可用的评价有’口味’, ‘环境’, ‘服务’, ‘人均消费’（‘点评数’也可以反映产品的受欢迎程度，但是其数据值比其他字段的对比要相差较多，而且其数据值本身波动范围较大），这里去掉’点评数’，添加一个‘性价比’字段的指标，假设：性价比 = （口味 + 环境 + 服务）/ 人均消费

data_filter = df[['类别', '口味', '环境', '服务', '人均消费']]
data_filter['性价比'] = (data_filter['口味'] + data_filter['环境'] + data_filter['服务']) / data_filter['人均消费']
data_filter.dropna(inplace = True)
data_filter = data_filter[(data_filter['口味']>0) & (data_filter['人均消费']>0)].reset_index()
del data_filter['index']
print(data_filter.head(15))

# –> 输出结果为：（首先选取所需要的指标字段，然后获得性价比指标字段的数据；再处理缺失值，这两步可以调整顺序，最后的数据之差只有三条（先处理缺失值是54886条数据，后处理缺失值是54889条数据），其次将数据为0的行数处理掉，这里只要’口味’, ‘环境’, '服务’中一项为0，其他的都为0，所以只选择一项即可；最后重新设置索引并删除原索引）

# 4. 绘制箱型图查看异常数据

# 由于数据量较大，对于异常值的处理就很有必要，首先进行异常值的查看，可以使用箱型图进行描述，这里最终选择 三个指标 对不同菜系进行比较（当然也可以把‘服务’加进来）

fig, axes = plt.subplots(1,3,figsize = (14,6))
ls_columns = [ '口味', '人均消费', "性价比"]
for i in range(len(ls_columns)):
    data_filter.boxplot(column=ls_columns[i], ax = axes[i] )

# –> 输出结果为：（这一部分就是matplotlib子图还有箱型图的绘制了，可以看到每个指标中都存在这大量的异常值）

# 5. 异常值数据的清洗工作

# 这里直接封装一个函数进行异常值的清洗，之后对于此类问题的处理可以直接进行函数的调用，而且处理各个字段的异常值应该分别进行处理，这样可以避免不同字段数据之间的影响

def f1(data,col):
    q1 = data[col].quantile(q = 0.25)
    q3 = data[col].quantile(q = 0.75) 
    iqr = q3-q1
    t1 = q1 - 3 * iqr
    t2 = q3 + 3 * iqr
    return data[(data[col] > t1)&(data[col]<t2)][['类别',col]]

data_kw = f1(data_filter,'口味')
data_rj = f1(data_filter,'人均消费')
data_xjb = f1(data_filter,'性价比')

# 使用iqr进行异常值的清洗，今后可以直接进行函数的调用，只需要修改一下‘类别’的信息即可

# 6. 数据标准化并排序

# 数据异常值处理完毕之后，标准化处理，还是一样直接封装函数，方便之后直接调用，依旧是对不同的数据进行标准化

def f2(data,col):
    col_name = col + '_norm'
    data_gp = data.groupby('类别').mean()
    data_gp[col_name] = (data_gp[col] - data_gp[col].min())/(data_gp[col].max()-data_gp[col].min())
    data_gp.sort_values(by = col_name, inplace = True, ascending=False)
    return data_gp

data_kw_score = f2(data_kw,'口味')
data_rj_score = f2(data_rj,'人均消费')
data_xjb_score = f2(data_xjb,'性价比')

# 标准化的基本步骤：首先创建一个新字段（列）并命名，然后按照某个要求进行分组（为什么取均值可以想一下，这个要回顾上一步异常值处理后的数据的结果），接着按照分组后的数据使用‘最大’/‘最小’标准化，最后进行某个字段（一般是某个标准化后的字段）进行排序即可

# 7. 数据合并与绘图前准备

# 经过异常值清洗和标准化处理，数据已经可以进行使用了。接着就是将分开处理的数据再合并在一起，因为存在三组数据，所以应该是两两合并（索引的标签都是餐馆的类型）

data_final_q1 = pd.merge(data_kw_score,data_rj_score,left_index=True,right_index=True)    # 首先合并口味、人均消费指标得分
data_final_q1 = pd.merge(data_final_q1,data_xjb_score,left_index=True,right_index=True)       # 接着合并性价比指标得分
print(data_final_q1.head(15))

# 使用bokeh绘图之前，需要将columns的数据设置为英文(index这一列的名称也要是英文)，另外设置一下点的大小（size参数）

data_final_q1['size'] = data_final_q1['口味_norm'] * 40  # 添加size字段
data_final_q1.index.name = 'type'
data_final_q1.columns = ['kw','kw_norm','price','price_norm','xjb','xjb_norm','size']

# 8. 出图

from bokeh.layouts import gridplot
from bokeh.models import HoverTool
from bokeh.models.annotations import BoxAnnotation

output_file('菜系类型.html')#输出文件
source = ColumnDataSource(data_final_q1)#创建数据
data_type = data_final_q1.index.tolist()#横坐标为index，要先转化为列表

hover = HoverTool(tooltips = [
    ('餐饮类型','@type'),
    ('人均消费','@price'),
    ('性价比得分','@xjb_norm'),
    ('口味得分','@kw_norm'),
])

result = figure(plot_width = 800,plot_height = 300,title = '餐饮类型得分',
				x_axis_label = '人均消费', y_axis_label = '性价比',
               tools = [hover, 'box_select, reset, xwheel_zoom,pan,crosshair'])
result.circle(x = 'price', y = 'xjb_norm', source = source,
			line_color ='black',line_dash =[6,4], fill_alpha =0.6,size = 'size')

price_mid = BoxAnnotation(left = 40, right = 80, fill_alpha = 0.1, fill_color = 'navy')
result.add_layout(price_mid)#这里设置标记区


kw = figure(plot_width = 800,plot_height = 300,title = '口味得分',x_range = data_type,
               tools = [hover, 'box_select, reset, xwheel_zoom,pan,crosshair'])
kw.vbar(x = 'type', top = 'kw_norm', source = source, width = 0.8, alpha = 0.7,color = 'red')

price = figure(plot_width = 800,plot_height = 300,title = '人均消费得分',x_range = data_type,
               tools = [hover, 'box_select, reset, xwheel_zoom,pan,crosshair'])
price.vbar(x = 'type', top = 'price_norm', source = source, width = 0.8, alpha = 0.7,color = 'green')

p = gridplot([[result],[kw],[price]])#将三个图放在一个画布上

show(p)#一定要加show（p）,否则不显示
