# help:如何使用查询功能：
# action_data数组，['type'] == 4]判断条件和值，[["user_id", "sku_id"]]输出字段
# action_data[action_data['type'] == 4][["user_id", "sku_id"]]

# 初始化
for i in [1]:
    # 导入数据分析包，绘图包
    import numpy, numpy.lib.recfunctions, pandas, matplotlib.pyplot
    # 初始化随机数函数deterministic (just a good practice)
    numpy.random.seed(1)  
    # 初始化logging
    import logging
    logging.basicConfig(level=logging.NOTSET)
    # 初始化时间日期格式
    import datetime
    from datetime import datetime
    def parse_dates(x):
        return numpy.datetime64(x)
    # 全局变量data_name表示你正在使用的是哪一个JData_Action文件，非常重要，不要随便改！(请在底下修改)
    data_name = 'JData_Action_0301_0315_FILE'
    # Jdata用来存放各种中间数据，这是一个字典，数据全在里面
    Jdata = {
        'dtype_info':{'JData_Action_0301_0315_FILE':{'user_id':numpy.int64,'sku_id':numpy.int64,'time':numpy.object,'model_id':numpy.float64,'type':numpy.int64,'cate':numpy.int64,'brand':numpy.int64,},'JData_Comment_line_by_day_FILE':{'sku_id':numpy.object,'comment_num':numpy.int64,'has_bad_comment':numpy.int64,'bad_comment_rate':numpy.float64,'comment_num.1':numpy.int64,'has_bad_comment.1':numpy.int64,'bad_comment_rate.1':numpy.float64,'comment_num.2':numpy.int64,'has_bad_comment.2':numpy.int64,'bad_comment_rate.2':numpy.float64,'comment_num.3':numpy.int64,'has_bad_comment.3':numpy.int64,'bad_comment_rate.3':numpy.float64,'comment_num.4':numpy.int64,'has_bad_comment.4':numpy.int64,'bad_comment_rate.4':numpy.float64,'comment_num.5':numpy.int64,'has_bad_comment.5':numpy.int64,'bad_comment_rate.5':numpy.float64,'comment_num.6':numpy.int64,'has_bad_comment.6':numpy.int64,'bad_comment_rate.6':numpy.float64,'comment_num.7':numpy.int64,'has_bad_comment.7':numpy.int64,'bad_comment_rate.7':numpy.float64,'comment_num.8':numpy.int64,'has_bad_comment.8':numpy.int64,'bad_comment_rate.8':numpy.float64,'comment_num.9':numpy.int64,'has_bad_comment.9':numpy.int64,'bad_comment_rate.9':numpy.float64,'comment_num.10':numpy.int64,'has_bad_comment.10':numpy.int64,'bad_comment_rate.10':numpy.float64,'comment_num.11':numpy.int64,'has_bad_comment.11':numpy.int64,'bad_comment_rate.11':numpy.float64,'comment_num.12':numpy.int64,'has_bad_comment.12':numpy.int64,'bad_comment_rate.12':numpy.float64,},'JData_Comment_FILE':{'dt':numpy.object,'sku_id':numpy.int64,'comment_num':numpy.int64,'has_bad_comment':numpy.int64,'bad_comment_rate':numpy.float64,},'JData_Product_FILE':{'sku_id':numpy.int64,'attr1':numpy.int64,'attr2':numpy.int64,'attr3':numpy.int64,'cate':numpy.int64,'brand':numpy.int64,},'JData_User_DONE_FILE':{'user_id':numpy.int64,'age':numpy.int64,'sex':numpy.int64,'user_lv_cd':numpy.int64,'user_reg_dt':numpy.int64,},'JData_Action_0301_0315_FILE_buy_user':{'user_id':numpy.int64,'sku_id':numpy.int64,},'JData_Action_0301_0315_FILE_ALL':{'user_id':numpy.int64,'sku_id':numpy.int64,'time':numpy.object,'model_id':numpy.float64,'type':numpy.int64,'cate_x':numpy.int64,'brand_x':numpy.int64,'comment_num':numpy.float64,'has_bad_comment':numpy.float64,'bad_comment_rate':numpy.float64,'comment_num.1':numpy.float64,'has_bad_comment.1':numpy.float64,'bad_comment_rate.1':numpy.float64,'comment_num.2':numpy.float64,'has_bad_comment.2':numpy.float64,'bad_comment_rate.2':numpy.float64,'comment_num.3':numpy.float64,'has_bad_comment.3':numpy.float64,'bad_comment_rate.3':numpy.float64,'comment_num.4':numpy.float64,'has_bad_comment.4':numpy.float64,'bad_comment_rate.4':numpy.float64,'comment_num.5':numpy.float64,'has_bad_comment.5':numpy.float64,'bad_comment_rate.5':numpy.float64,'comment_num.6':numpy.float64,'has_bad_comment.6':numpy.float64,'bad_comment_rate.6':numpy.float64,'comment_num.7':numpy.float64,'has_bad_comment.7':numpy.float64,'bad_comment_rate.7':numpy.float64,'comment_num.8':numpy.float64,'has_bad_comment.8':numpy.float64,'bad_comment_rate.8':numpy.float64,'comment_num.9':numpy.float64,'has_bad_comment.9':numpy.float64,'bad_comment_rate.9':numpy.float64,'comment_num.10':numpy.float64,'has_bad_comment.10':numpy.float64,'bad_comment_rate.10':numpy.float64,'comment_num.11':numpy.float64,'has_bad_comment.11':numpy.float64,'bad_comment_rate.11':numpy.float64,'comment_num.12':numpy.float64,'has_bad_comment.12':numpy.float64,'bad_comment_rate.12':numpy.float64,'attr1':numpy.int64,'attr2':numpy.int64,'attr3':numpy.int64,'cate_y':numpy.int64,'brand_y':numpy.int64,'age':numpy.int64,'sex':numpy.int64,'user_lv_cd':numpy.int64,'user_reg_dt':numpy.int64,},'JData_Action_0301_0315_FILE_ALL_buy_user':{'user_id':numpy.int64,'sku_id':numpy.int64,}},
        'info': {
            'JData_Action_0301_0315_FILE':
            ['user_id', 'sku_id', 'time', 'model_id', 'type', 'cate', 'brand'],
            'JData_Comment_line_by_day_FILE': [
                'sku_id', 'comment_num', 'has_bad_comment', 'bad_comment_rate',
                'comment_num.1', 'has_bad_comment.1', 'bad_comment_rate.1',
                'comment_num.2', 'has_bad_comment.2', 'bad_comment_rate.2',
                'comment_num.3', 'has_bad_comment.3', 'bad_comment_rate.3',
                'comment_num.4', 'has_bad_comment.4', 'bad_comment_rate.4',
                'comment_num.5', 'has_bad_comment.5', 'bad_comment_rate.5',
                'comment_num.6', 'has_bad_comment.6', 'bad_comment_rate.6',
                'comment_num.7', 'has_bad_comment.7', 'bad_comment_rate.7',
                'comment_num.8', 'has_bad_comment.8', 'bad_comment_rate.8',
                'comment_num.9', 'has_bad_comment.9', 'bad_comment_rate.9',
                'comment_num.10', 'has_bad_comment.10', 'bad_comment_rate.10',
                'comment_num.11', 'has_bad_comment.11', 'bad_comment_rate.11',
                'comment_num.12', 'has_bad_comment.12', 'bad_comment_rate.12'
            ],
            'JData_Comment_FILE':
            ['dt', 'sku_id', 'comment_num', 'has_bad_comment', 'bad_comment_rate'],
            'JData_Product_FILE':
            ['sku_id', 'attr1', 'attr2', 'attr3', 'cate', 'brand'],
            'JData_User_DONE_FILE':
            ['user_id', 'age', 'sex', 'user_lv_cd', 'user_reg_dt'],
            'JData_Action_0301_0315_FILE_buy_user': ['user_id', 'sku_id'],
            'JData_Action_0301_0315_FILE_ALL':['user_id', 'sku_id', 'time', 'model_id', 'type', 'cate_x', 'brand_x',
        'comment_num', 'has_bad_comment', 'bad_comment_rate', 'comment_num.1',
        'has_bad_comment.1', 'bad_comment_rate.1', 'comment_num.2',
        'has_bad_comment.2', 'bad_comment_rate.2', 'comment_num.3',
        'has_bad_comment.3', 'bad_comment_rate.3', 'comment_num.4',
        'has_bad_comment.4', 'bad_comment_rate.4', 'comment_num.5',
        'has_bad_comment.5', 'bad_comment_rate.5', 'comment_num.6',
        'has_bad_comment.6', 'bad_comment_rate.6', 'comment_num.7',
        'has_bad_comment.7', 'bad_comment_rate.7', 'comment_num.8',
        'has_bad_comment.8', 'bad_comment_rate.8', 'comment_num.9',
        'has_bad_comment.9', 'bad_comment_rate.9', 'comment_num.10',
        'has_bad_comment.10', 'bad_comment_rate.10', 'comment_num.11',
        'has_bad_comment.11', 'bad_comment_rate.11', 'comment_num.12',
        'has_bad_comment.12', 'bad_comment_rate.12', 'attr1', 'attr2', 'attr3',
        'cate_y', 'brand_y', 'age', 'sex', 'user_lv_cd', 'user_reg_dt'],
        }
    }
    #准备文件
    JData_Action = {
        'JData_Action_':
        ['user_id', 'sku_id', 'time', 'model_id', 'type', 'cate', 'brand'],
        'user_id':
        ' 用户编号',
        'sku_id':
        '商品编号',
        'time':
        ' 行为时间',
        'model_id':
        '点击模块编号，如果是点击',
        'type':
        ' 1.浏览（指浏览商品详情页）；2.加入购物车；3.购物车删除；4.下单；5.关注；6.点击',
        'cate':
        '品类ID',
        'brand':
        '品牌ID'
    }
    path = 'D:\PythonApplication1\PythonApplication1\deeplearning\JDdata'
    FILE = {
        'JData_Action_0301_0315_FILE':
        path + '\data\JData_Action_0301_0315.csv',
        #'JData_Action_0316_0331_FILE':
        #path + '\data\JData_Action_0316_0331.csv',
        #'JData_Action_0401_0415_FILE':
        #path + '\data\JData_Action_0401_0415.csv',
        'JData_Comment_line_by_day_FILE':
        path + '\data\JData_Comment_line_by_day.csv',
        'JData_Comment_FILE':
        path + '\data\JData_Comment.csv',
        'JData_Product_FILE':
        path + '\data\JData_Product.csv',
        #'JData_User_FILE':
        #path + '\data\JData_User.csv',
        'JData_User_DONE_FILE':
        path + '\data\JData_User_DONE.csv'
    }
    FILE_ACTION = {
        'JData_Action_0301_0315_FILE': path + '\data\JData_Action_0301_0315.csv',
        #'JData_Action_0316_0331_FILE':
        #path + '\data\JData_Action_0316_0331.csv',
        #'JData_Action_0401_0415_FILE':
        #path + '\data\JData_Action_0401_0415.csv',
    }


#读取csv文件
def get_data(fname, chunk_size=102401):#,i=None):
    # 为什么读入数据的时候不直接df = pandas.read_csv(fname, header=0, usecols=["sku_id", "type"])
    # 因为文件太大了
    reader = pandas.read_csv(
        fname, header=0, iterator=True, infer_datetime_format=True)#,dtype=Jdata['dtype_info'][i],date_parser=parse_dates) # 这里的i是前面循环的FILE，就是Jdata的名字
    chunks = []
    loop = True
    i = 0
    while loop:
        if i==300:loop = False # 电脑内存小跑得慢，实战注释掉。
        try:
            i = i + 1
            logging.warning('loop:' + str(i))
            chunk = reader.get_chunk(chunk_size)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            logging.warning(
                str(StopIteration) + "（读取完毕）Iteration is stopped" + 'loop:' +
                str(i))
        except KeyboardInterrupt:
            loop = False
            logging.warning(
                str(KeyboardInterrupt) +
                "（读取手动中断）Iteration is stopped，中断读取，开始下一步" + 'loop:' + str(
                    i))
    df_ac = pandas.concat(chunks, ignore_index=True)
    # 转时间日期格式
    try:
        df_ac['time']=pandas.to_datetime(df_ac['time'])
    except KeyError:
        print()
    try:
        df_ac['dt']=pandas.to_datetime(df_ac['dt'])
    except KeyError:
        print()
    return df_ac


#让我看看谁买了东西（请输入Action数据）
def find_buy_user(action_data=[],
                    is_save=False,
                    savepath=path + '\\save.csv'):
    buy_user = []
    #　在一个文件中寻找有购买记录的用户－商品对buy_user
    buy_user = action_data[action_data['type'] == 4][["user_id", "sku_id"]].drop_duplicates('user_id')
    # 去除重复用户  返回购买的人和商品"user_id", "sku_id"
    if is_save:  # 辛辛苦苦出有购买记录的用户，要保存，要写写到csv文件
        Jdata[data_name + '_buy_user'] = buy_user
        Jdata[data_name + '_buy_user'].to_csv(
            savepath,
            index=False)  #path+'\\data\\BUY_USER_LIST_'+data_name+'.CSV'
    return buy_user

#让我看看谁小气到抠门，啥都没买（请输入Action数据）
def find_unbuy_user(action_data=[],
                    is_save=False,
                    savepath=path + '\\save.csv'):
    pass

#预处理Action数据（主要是找出谁买了东西）：
def run(data_name=data_name):
    Jdata[data_name + '_buy_user'] = find_buy_user(
        Jdata[data_name],
        is_save=True,
        savepath=path + '\\data\\BUY_USER_LIST_' + data_name + '.CSV')
    # FILE_ACTION太大了要处理掉不然太占内存
    # 舍不得处理
    # Jdata[data_name+'_buy_user']=[]
    # Jdata[data_name]=[]


#高潜用户行为轨迹分析
#让我看看这个用户干嘛了
def user_action(Jdata_name='JData_Action_0301_0315_FILE',
                user_id=144121,
                is_save=False,
                savepath=path + '\\save.csv'):
    buy_user = []
    buy_user = Jdata[Jdata_name][Jdata[Jdata_name]['user_id'] == user_id][
        Jdata['info'][Jdata_name]]
    if buy_user.size == 0:
        return None
    if is_save:
        Jdata[data_name + '_user_action_data'][user_id] = buy_user
        # 别保存文件了，文件太多太大
        # Jdata[data_name + 'user_action'].to_csv(savepath,index=False)  #path+'\\data\\BUY_USER_LIST_'+data_name+'.CSV'
    return buy_user


#画图
def paint_user_action(user_id=144121, show=False):
    cu_record = Jdata[data_name + '_user_action_data'][user_id]
    time_range = pandas.to_datetime(
        cu_record['time']).map(lambda x: x.strftime('%m-%d %H:%M'))
    x_index = range(len(cu_record['type']))
    # 设置图片大小
    matplotlib.pyplot.figure(figsize=(18, 5))
    matplotlib.pyplot.scatter(
        x_index,
        cu_record['type'],
        c=cu_record['type'],
        s=36,
        lw=0,
        cmap=matplotlib.pyplot.cm.coolwarm)
    matplotlib.pyplot.plot(x_index, cu_record['type'], 'y--', markersize=1)
    matplotlib.pyplot.xlim(min(x_index) - 1, max(x_index) + 1)
    matplotlib.pyplot.ylim(0, 7)
    matplotlib.pyplot.xlabel('number')
    matplotlib.pyplot.ylabel('behavior')
    # matplotlib.pyplot.xticks(range(len(cu_record['type'])), time_range, rotation='vertical', fontsize=8)
    matplotlib.pyplot.yticks(
        range(0, 8),
        ["", "browse", "add cart", "del cart", "buy", "favor", "click"])
    matplotlib.pyplot.tight_layout()
    if show: matplotlib.pyplot.show()  #显示窗口
    return


# 读取数据
for i in FILE:
    logging.warning(i)
    Jdata[i] = get_data(FILE[i])#,i=i)

# for data_name in FILE_ACTION:
# 预处理Action数据：
run(data_name)
'''
# 合并A,C,P,U（基于A），制作行为+评论+商品+用户宽表
for i in [1]:
    print('合并数据，慢')
    try:
        A = Jdata[data_name]
        C = Jdata['JData_Comment_line_by_day_FILE']
        P = Jdata['JData_Product_FILE']
        U = Jdata['JData_User_DONE_FILE']
        tem = pandas.merge(A, C, how='left', on='sku_id')
        tem = pandas.merge(tem, P, on='sku_id')
        print('最后一步啦')
        Jdata[data_name+'_ALL'] = pandas.merge(tem, U, on='user_id')
        #把购买记录也复制到_ALL里面
        Jdata[data_name + '_ALL_buy_user']=Jdata[data_name + '_buy_user']
    except KeyboardInterrupt:
        logging.warning(
            str(KeyboardInterrupt) +
            "（合并数据手动中断）Iteration is stopped，中断合并数据，开始下一步" + 'loop:' + str(
                data_name))
    finally:
        data_name =data_name+'_ALL'
'''

# 按每个用户分表
Jdata[data_name + '_user_action_data'] = {}
for user_id in Jdata[data_name + '_buy_user']['user_id']:
    Jdata[data_name + '_user_action_data'][user_id] = user_action(
        Jdata_name=data_name, user_id=user_id)
# 拿最后5天记录
def get_last_5_days(user_id,data_name=data_name,last_day=numpy.datetime64('2016-04-01 00:00:00')):
    last_5_day=last_day-numpy.timedelta64(1,'D')
    a=[]
    a=Jdata[data_name + '_user_action_data'][user_id]
    last_day=numpy.datetime64(a['time'].max())    
    last_5_day=last_day-numpy.timedelta64(1,'D')
    a=a[(a.time>last_5_day)]
    return a

# 最后5天买东西了吗？
def is_buy_last_5_days(a): # 先调用get_last_5_days，再调用这个
    return not a[(a.type == 4)].empty # 最后5天是否有购买记录？

# 最后5天买啥了？
def buy_what_in_last_5_days(a): # 先调用get_last_5_days，再调用这个
    return a[(a.type == 4)].sku_id.max() # 最后5天是否有购买记录？

# 我就是不告诉神经网络最后5天用户干嘛了
def deleted_last_5_days_data(user_id,data_name=data_name,last_5_day=numpy.datetime64('2016-04-01 00:00:00')):
    a=[]
    a=Jdata[data_name + '_user_action_data'][user_id]
    return a[(a.time<last_5_day)]


# df.iterrows()，对DataFrame的每一行进行迭代，返回一个Tuple (index, Series)
# df.itertuples()，也是一行一行地迭代，返回的是一个namedtuple，通常比iterrow快，因为不需要做转换

# 神经网络的食物：Jdata[data_name + '_user_action_data'][user_id]，每一个有购买记录的人，都是食物。
def train(X,Y):
    pass

#run(data_name)
print('the end')
