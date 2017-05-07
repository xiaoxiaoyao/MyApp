#导入数据分析包，绘图包
import numpy, pandas, matplotlib.pyplot
#初始化logging
import logging
logging.basicConfig(level=logging.NOTSET)
#初始化循环用的i
loop_i = 0
# Jdata用来存放各种中间数据，这是一个字典，数据全在里面
Jdata = {
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
        'JData_Action_0301_0315_FILEbuy_user': ['user_id', 'sku_id']
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
def get_data(fname, chunk_size=100001):
    # 为什么读入数据的时候不直接df = pandas.read_csv(fname, header=0, usecols=["sku_id", "type"])
    # 因为文件太大了
    reader = pandas.read_csv(fname, header=0, iterator=True)
    chunks = []
    loop = True
    loop_i = 0
    while loop:
        try:
            loop_i = loop_i + 1
            logging.warning('loop:' + str(loop_i))
            chunk = reader.get_chunk(chunk_size)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            logging.warning(
                str(StopIteration) + "（读取完毕）Iteration is stopped" + 'loop:' +
                str(loop_i))
        except KeyboardInterrupt:
            loop = False
            logging.warning(
                str(KeyboardInterrupt) +
                "（读取手动中断）Iteration is stopped，中断读取，开始下一步" + 'loop:' + str(
                    loop_i))
    df_ac = pandas.concat(chunks, ignore_index=True)
    return df_ac


#预处理Action数据（主要是找出谁买了东西）：
def run(loop_i):
    #让我看看谁买了东西（请输入Action数据）
    def find_buy_user(action_data=[],
                      is_save=False,
                      savepath=path + '\\save.csv'):
        buy_user = []
        #　在一个文件中寻找有购买记录的用户－商品对buy_user
        buy_user = action_data[action_data['type'] == 4][
            ["user_id", "sku_id"]].drop_duplicates('user_id')
        # 去除重复用户  返回购买的人和商品"user_id", "sku_id"
        if is_save:  # 辛辛苦苦出有购买记录的用户，要保存，要写写到csv文件
            Jdata[loop_i + 'buy_user'] = buy_user
            Jdata[loop_i + 'buy_user'].to_csv(
                savepath,
                index=False)  #path+'\\data\\BUY_USER_LIST_'+loop_i+'.CSV'
        return Jdata[loop_i + 'buy_user']

    #让我看看谁小气到抠门，啥都没买（请输入Action数据）
    def find_unbuy_user(action_data=[],
                        is_save=False,
                        savepath=path + '\\save.csv'):
        pass

    Jdata[loop_i + 'buy_user'] = find_buy_user(
        Jdata[loop_i],
        is_save=True,
        savepath=path + '\\data\\BUY_USER_LIST_' + loop_i + '.CSV')
    # FILE_ACTION太大了要处理掉不然太占内存
    # 舍不得处理
    # Jdata[loop_i+'buy_user']=[]
    # Jdata[loop_i]=[]


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
        Jdata[loop_i + '_user_action_data'][user_id] = buy_user
        # 别保存文件了，文件太多太大
        # Jdata[loop_i + 'user_action'].to_csv(savepath,index=False)  #path+'\\data\\BUY_USER_LIST_'+loop_i+'.CSV'
    return buy_user


#画图
def paint_user_action(user_id=144121, show=False):
    cu_record = Jdata[loop_i + '_user_action_data'][user_id]
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
for loop_i in FILE:
    logging.warning(loop_i)
    Jdata[loop_i] = get_data(FILE[loop_i])

# 全局变量loop_i表示你正在使用的是哪一个JData_Action文件，非常重要，不要随便改！
loop_i = 'JData_Action_0301_0315_FILE'
# for loop_i in FILE_ACTION:
# 预处理Action数据：
run(loop_i)

Jdata[loop_i + '_user_action_data'] = {}
# 实战时使用
# for user_id in Jdata['JData_User_DONE_FILE']['user_id']:
# 调试时间使用
for user_id in Jdata[loop_i + 'buy_user']['user_id']:
    Jdata[loop_i + '_user_action_data'][user_id] = user_action(
        Jdata_name=loop_i, user_id=user_id)
