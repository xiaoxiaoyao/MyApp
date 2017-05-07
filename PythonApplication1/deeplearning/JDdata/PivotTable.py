#导入数据分析包，绘图包
import numpy, pandas, matplotlib
#初始化logging
import logging
logging.basicConfig(level=logging.NOTSET)
#初始化循环用的i
loop_i = 0
# Jdata用来存放各种中间数据，这是一个字典
Jdata={}

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
    '品牌ID'}
path = 'D:\PythonApplication1\PythonApplication1\deeplearning\JDdata'
FILE = {
    'JData_Action_0301_0315_FILE':
    path + '\data\JData_Action_0301_0315.csv',
    'JData_Action_0316_0331_FILE':
    path + '\data\JData_Action_0316_0331.csv',
    'JData_Action_0401_0415_FILE':
    path + '\data\JData_Action_0401_0415.csv',
    'JData_Comment_line_by_day_FILE':
    path + '\data\JData_Comment_line_by_day.csv',
    'JData_Comment_FILE':
    path + '\data\JData_Comment.csv',
    'JData_Product_FILE':
    path + '\data\JData_Product.csv',
    #'JData_User_FILE':
    #path + '\data\JData_User.csv',
    'JData_User_DONE_FILE':
    path + '\data\JData_User_DONE.csv'}
FILE_ACTION={'JData_Action_0301_0315_FILE':
    path + '\data\JData_Action_0301_0315.csv',
    #'JData_Action_0316_0331_FILE':
    #path + '\data\JData_Action_0316_0331.csv',
    #'JData_Action_0401_0415_FILE':
    #path + '\data\JData_Action_0401_0415.csv',
    }
#读取csv文件
def get_data(fname,chunk_size=100001):
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
                str(StopIteration) + "（读取完毕）Iteration is stopped" + 'loop:' + str(
                    loop_i))
        except KeyboardInterrupt:
            loop = False
            logging.warning(
                str(KeyboardInterrupt) + "（读取手动中断）Iteration is stopped，中断读取，开始下一步" +
                'loop:' + str(loop_i))
    df_ac = pandas.concat(chunks, ignore_index=True)
    return df_ac


#让我看看谁买了东西（请输入Action数据）
def find_buy_user(action_data=[]):
    buy_user=[]
    #　在一个文件中寻找有购买记录的用户－商品对buy_user
    buy_user=action_data[action_data['type'] == 4][["user_id", "sku_id"]]
    # 去除重复用户  返回购买的人和商品"user_id", "sku_id"
    return buy_user.drop_duplicates('user_id')


#预处理Action数据：
def run(loop_i):
    logging.warning(loop_i)
    Jdata[loop_i] = get_data(FILE[loop_i])
    Jdata[loop_i+'buy_user']=find_buy_user(Jdata[loop_i])
    # 辛辛苦苦出有购买记录的用户，要保存，要写写到csv文件
    Jdata[loop_i+'buy_user'].to_csv(path+'\\data\\BUY_USER_LIST_'+loop_i+'.CSV', index=False)
    # FILE_ACTION太大了要处理掉不然太占内存
    # 舍不得处理
    # Jdata[loop_i+'buy_user']=[]
    # Jdata[loop_i]=[]
# 读取数据
# for loop_i in FILE_ACTION:
#    run(loop_i)
loop_i=0
