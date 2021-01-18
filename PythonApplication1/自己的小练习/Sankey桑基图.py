from pyecharts.charts import Sankey
from pyecharts import options as opts

linkes=[
{'source':'03万','target':'续费后03万','value':20},
{'source':'03万','target':'续费后05万','value':70},
{'source':'03万','target':'续费后10万','value':25},
{'source':'03万','target':'续费后15万','value':12},
{'source':'03万','target':'续费后25万','value':10},
{'source':'03万','target':'续费后50万','value':4},
{'source':'03万','target':'续费后包年','value':2},
{'source':'05万','target':'续费后03万','value':6},
{'source':'05万','target':'续费后05万','value':139},
{'source':'05万','target':'续费后10万','value':157},
{'source':'05万','target':'续费后15万','value':91},
{'source':'05万','target':'续费后25万','value':48},
{'source':'05万','target':'续费后50万','value':6},
{'source':'05万','target':'续费后包年','value':8},
{'source':'05万','target':'续费后单价极低','value':1},
{'source':'10万','target':'续费后03万','value':3},
{'source':'10万','target':'续费后05万','value':5},
{'source':'10万','target':'续费后10万','value':22},
{'source':'10万','target':'续费后15万','value':73},
{'source':'10万','target':'续费后25万','value':39},
{'source':'10万','target':'续费后50万','value':21},
{'source':'10万','target':'续费后包年','value':5},
{'source':'10万','target':'续费后单价极低','value':2},
{'source':'15万','target':'续费后03万','value':3},
{'source':'15万','target':'续费后05万','value':3},
{'source':'15万','target':'续费后10万','value':2},
{'source':'15万','target':'续费后15万','value':56},
{'source':'15万','target':'续费后25万','value':73},
{'source':'15万','target':'续费后50万','value':46},
{'source':'15万','target':'续费后包年','value':12},
{'source':'15万','target':'续费后单价极低','value':7},
{'source':'25万','target':'续费后10万','value':1},
{'source':'25万','target':'续费后25万','value':49},
{'source':'25万','target':'续费后50万','value':46},
{'source':'25万','target':'续费后包年','value':40},
{'source':'25万','target':'续费后单价极低','value':25},
{'source':'50万','target':'续费后25万','value':2},
{'source':'50万','target':'续费后50万','value':17},
{'source':'50万','target':'续费后包年','value':7},
{'source':'50万','target':'续费后单价极低','value':11},
{'source':'包年','target':'续费后03万','value':1},
{'source':'包年','target':'续费后05万','value':7},
{'source':'包年','target':'续费后10万','value':2},
{'source':'包年','target':'续费后15万','value':6},
{'source':'包年','target':'续费后25万','value':5},
{'source':'包年','target':'续费后50万','value':5},
{'source':'包年','target':'续费后包年','value':109},
{'source':'包年','target':'续费后单价极低','value':15},
{'source':'单价极低','target':'续费后包年','value':2},
{'source':'单价极低','target':'续费后单价极低','value':4},
]

nodes=[
{'name':'03万'},
{'name':'05万'},
{'name':'10万'},
{'name':'15万'},
{'name':'25万'},
{'name':'50万'},
{'name':'包年'},
{'name':'单价极低'},
{'name':'续费后03万'},
{'name':'续费后05万'},
{'name':'续费后10万'},
{'name':'续费后15万'},
{'name':'续费后25万'},
{'name':'续费后50万'},
{'name':'续费后包年'},
{'name':'续费后单价极低'},
]

pic = (
    Sankey()
    .add('', #图例名称
         nodes,    #传入节点数据
         linkes,   #传入边和流量数据
         #设置透明度、弯曲度、颜色
         linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = "source"),
         #标签显示位置
         label_opts=opts.LabelOpts(position="right"),
         #节点之前的距离
         node_gap = 30,
         # 鼠标 hover 到节点或边上，相邻接的节点和边高亮的交互，默认关闭，可手动开启
         focus_node_adjacency="allEdges"
    )
    .set_global_opts(title_opts=opts.TitleOpts(title = '企业版合同续签客户流向'))
)
#输出文件
pic.render(r'C:\Users\YAO\AppData\Local\Temp\test.html')
