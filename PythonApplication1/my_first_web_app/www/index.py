# -*- coding: utf-8 -*-
"""
Flask Web 应用主文件
实现博客、数据库展示和匿名微博功能
"""

import io
from flask import Flask, render_template, g, request, url_for, session, redirect, abort, logging
import config
import conn

### 初始化程序
global app
app = Flask(__name__)

### 初始化数据链接
global appconn
appconn = conn.Conn(app)

### 博客数据（示例数据，后续可改为数据库存储）
blog_posts = [
    {
        'id': 1,
        'title': '我的第一篇博客文章!',
        'summary': '我是一个税务师，想转行做编程，于是从PYTHON入手。为了学习PYTHON，我安装了PYTHON，安装了以后不知道学什么，看到别人学数据库，装了一个MYSQL。',
        'content': '我是一个税务师，想转行做编程，于是从PYTHON入手。为了学习PYTHON，我安装了PYTHON，安装了以后不知道学什么，看到别人学数据库，装了一个MYSQL。数据库装了好像没什么用处，然后又看到别人学了flask，感觉这是一条路，就开始PYTHON的WEB之路。作为税务师，转行不容易，希望自己加油，虽然知道自己一边做税务师一边学编程挺困难，但是么，还是喜欢。'
    },
    {
        'id': 2,
        'title': 'Hello, bootstrap!',
        'summary': 'bootstrap这是一个可视化布局模板, 你可以点击模板里的文字进行修改, 也可以通过点击弹出的编辑框进行富文本修改.',
        'content': 'bootstrap这是一个可视化布局模板, 你可以点击模板里的文字进行修改, 也可以通过点击弹出的编辑框进行富文本修改. 拖动区块能实现排序.'
    },
    {
        'id': 3,
        'title': 'Hello, python!',
        'summary': 'Python is a programming language that lets you work quickly and integrate systems more effectively.',
        'content': 'Python is a programming language that lets you work quickly and integrate systems more effectively.'
    },
    {
        'id': 4,
        'title': 'Hello, flask!',
        'summary': 'Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. Flask 是一个 Python 实现的 Web 开发微框架。'
    }
]


### 测试模块
@app.route('/test', methods=("GET", "POST"))
def Test():
    """测试模块，用于验证应用和数据库连接。

    Returns:
        渲染后的测试页面
    """
    app.logger.info("next is app and appconn")
    app.logger.info(app)
    app.logger.info(appconn)
    cur = conn.Select_table(appconn, '*')
    return render_template('base.html', info=config.info, language=cur.fetchall())

### 首页 - 博客列表
@app.route('/')
@app.route('/<name>')
def Index(name=None):
    """首页，显示博客文章列表。

    Args:
        name: 可选的名称参数

    Returns:
        渲染后的博客列表页面
    """
    return render_template('blog_list.html', info=config.info, posts=blog_posts, name=name)


### 博客详情页
@app.route('/blog/<int:id>')
def Blog(id=0):
    """博客详情页，显示完整的博客文章。

    Args:
        id: 博客文章ID

    Returns:
        渲染后的博客详情页面
    """
    post = next((p for p in blog_posts if p['id'] == id), None)
    if post is None:
        abort(404)
    return render_template('blog_detail.html', info=config.info, post=post)
### 数据库演示页跳转页
@app.route('/database/<database>')
def Databasegoto(database=None):
    """数据库演示页跳转页，跳转到指定数据库的默认表。

    Args:
        database: 数据库名称

    Returns:
        重定向到数据库展示页
    """
    app.logger.info("Go to DataGet(table='actor',database='sakila'):")
    return redirect(url_for('DataGet', database='sakila', table='actor'))


### 数据库展示页
@app.route('/database/<database>/<table>', methods=("GET",))
def DataGet(table='actor', database='sakila'):
    """数据库展示页，显示指定表的数据。

    Args:
        table: 表名，默认为 'actor'
        database: 数据库名，默认为 'sakila'

    Returns:
        渲染后的数据库展示页面
    """
    assert request.method == 'GET'
    row = request.args.get('row', '*')
    cur = conn.Select_table(appconn, row, table)
    tables = conn.Show_tables(appconn)
    pass
    return render_template('database.html', info=config.info, data=cur, database=database, table=table, tables=tables, row=row)


### 数据库插入
@app.route('/database/<database>/<table>', methods=("POST",))
def DataPost(table='actor', database='sakila'):
    """数据库插入操作，向指定表插入数据。

    Args:
        table: 表名，默认为 'actor'
        database: 数据库名，默认为 'sakila'

    Returns:
        操作结果字符串
    """
    assert request.method == 'POST'
    a = []
    a.append(request.get_data())
    a.append(request.form.getlist('Table')[0])
    description = conn.description(appconn, str(request.form.getlist('Table')[0]))
    a.append(description)
    a.append(request.form)
    values = []
    rows = []

    try:
        for row in description:
            values.append(request.form['Row_' + str(row[0])])
            rows.append(row[0])
    except:
        print('err')
        return
    else:
        value = [rows, values]
        print('value!!!', value)
        conn.Insert(appconn, database, table, value)
        return str(a)

### 微博数据（示例数据，后续可改为数据库存储）
weibo_list = [
    {
        'id': 1,
        'username': '用户A',
        'content': 'W3CSCHOOL 菜鸟教程，学的不仅是技术，更是梦想！',
        'ip': '192.168.1.1',
        'time': '2024-01-01 10:00:00'
    },
    {
        'id': 2,
        'username': '用户B',
        'content': 'Python 是一门很棒的编程语言！',
        'ip': '192.168.1.2',
        'time': '2024-01-01 11:00:00'
    }
]


### 微博功能 - 显示列表
@app.route('/weibo/<int:id>')
def Weibo(id=0):
    """微博页面，显示微博列表。

    Args:
        id: 可选的微博ID参数

    Returns:
        渲染后的微博页面
    """
    return render_template('weibo.html', info=config.info, weibo_list=weibo_list)


### 微博功能 - 发布微博
@app.route('/weibo/post', methods=['POST'])
def WeiboPost():
    """发布新微博。

    Returns:
        重定向到微博列表页面
    """
    from datetime import datetime
    
    username = request.form.get('username', '匿名用户')
    content = request.form.get('content', '')
    
    if content and len(content) <= 140:
        new_weibo = {
            'id': len(weibo_list) + 1,
            'username': username,
            'content': content,
            'ip': request.remote_addr,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        weibo_list.insert(0, new_weibo)
    
    return redirect(url_for('Weibo', id=0))

### 启动主程序
if __name__ == '__main__':
    """主程序入口。

    配置Flask应用，启动调试工具栏，运行Web服务器。
    """
    app.config.from_pyfile('config.py')
    # conn.TestConn(app)
    # 据说很方便的调试工具，该扩展为 Flask 应用程序添加了一个包含有用的调试信息的工具栏。
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)
    app.run()
    # 关闭连接
    conn.Close(appconn)
    # 结束程序
    print('Thank you')
