# 申明：该爬虫与本人工作经历、任职公司无关，完全出于个人兴趣。

import requests,re
# 用来获取商品列表
def find_product_id(key_word="胸罩",page=3):
    '''
    *@Function【查询商品id】    首先我们需要在搜索页面获取商品的id，为下面爬取用户评价提供productId.
    *@Request: 请求 [in]
    *   param1  string key_word: key_word为搜索的关键字
    *@Response：响应 [out]
    *   param1 int page: page为爬取页数默认爬前3页的商品
    *@Return：返回值 product_ids = [] :  商品 ID
    '''
    jd_url = 'https://search.jd.com/Search'
    product_ids = []
    # 爬前3页的商品
    for i in range(1,page):
        param = {'keyword': key_word, 'enc': 'utf-8', 'page': i}
        response = requests.get(jd_url, params=param)
        # 商品id
        ids = re.findall('data-pid="(.*?)"', response.text, re.S)
        product_ids += ids
    return product_ids

import json,threading
def get_comment_message(product_id='15752689550',pages=11):
    '''
    获取评论内容
    '''
    urls = ['https://sclub.jd.com/comment/productPageComments.action?' \
            'callback=fetchJSON_comment98vv53282&' \
            'productId={}' \
            '&score=0&sortType=5&' \
            'page={}' \
            '&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(product_id, page) for page in range(1, pages)] # 拼接 URL
    for url in urls:
        html = requests.get(url).text.replace('fetchJSON_comment98vv53282(', '').replace(');', '')
        data = json.loads(html)
        for comment in data['comments']:
            # flush_data清洗数据的方法
            comment['productColor'] = flush_data(comment['productColor'])
            # size
            comment['productSize'] = flush_data(comment['productSize'])
            yield comment # 惰性计算，满速返回

#  因为每种商品的颜色、尺寸描述上有差异，为了方面统计，我们进行了简单的数据清洗。
def flush_data(data='肤'): # 一键替换同义词；
    return {
        '肤' : '肤色', '果绿色':'绿色','黑' : '黑色', '紫' : '紫色', '粉' : '粉色', '蓝' : '蓝色', '白' : '白色', '灰' : '灰色', '槟' : '香槟色', '琥' : '琥珀色', '红' : '红色', 'A' : 'A', 'B' : 'B', 'C' : 'C', 'D' : 'D'
    }.get(data, data)

def spider_jd(ids):
    while ids:
        # 加锁
        lock.acquire()
        # 取出第一个元素
        id = ids[0]
        # 将取出的元素从列表中删除，避免重复加载
        del ids[0]
        # 释放锁
        lock.release()
        # 获取评论内容
        for i in get_comment_message(id,3):
            save_data(i)

#决定如何保存数据
def save_data(data={}):
    # 保存数据的方法
    pymongo_save_data(data)

# python的单例模式就是一个类的实例只能自始自终自能创建一次。应用场景比如说数据库的连接池。
import pymongo
# mongo服务
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?safe=true')# 仅限本机，不留 password
# jd数据库
db = client.jd
def pymongo_save_data(data={}):
    global client,db
    # product表,没有自动创建，写数据库
    print(data)
    db.product.insert(data)

if __name__=='__main__':
    lock = threading.Lock()
    product_ids = find_product_id('胸罩')
    for i in range(1):
        # 增加一个获取评论的线程
        t = threading.Thread(target=spider_jd, args=(find_product_id('胸罩'),))
        # 启动线程.这里预先使用多线程。
        t.start()
