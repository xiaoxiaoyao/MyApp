# -*- coding: utf-8 -*-
import io
from flask import Flask, render_template, g , request, url_for, session, redirect, abort, logging
import config,conn
###初始化程序
global app
app = Flask(__name__)

###初始化数据链接
global appconn
appconn=conn.Conn(app)


###测试模块
@app.route('/test', methods=("GET", "POST"))
def Test():
    app.logger.info("next is app and appconn")
    app.logger.info(app)
    app.logger.info(appconn)
    cur=conn.Select_table(appconn,'*')
    return render_template('base.html',info=config.info,language=cur.fetchall())

###首页
@app.route('/')
@app.route('/<name>')
def Index(name=None):
    return render_template('home.html',info=config.info, name=name)

###数据库演示页跳转页
@app.route('/database/<database>')
def Databasegoto(database=None):
    app.logger.info("Go to DataGet(table='actor',database='sakila'):")
    return redirect(url_for('DataGet',database='sakila', table='actor'))

###数据库展示页
@app.route('/database/<database>/<table>',methods=("GET",))
def DataGet(table='actor',database='sakila'):
    assert request.method == 'GET'
    row=request.args.get('row', '*')
    cur=conn.Select_table(appconn,row,table)
    tables=conn.Show_tables(appconn)
    pass
    return render_template('database.html',info=config.info, data=cur,database=database,table=table,tables=tables,row=row)
###数据库插入
@app.route('/database/<database>/<table>',methods=("POST",))
def DataPost(table='actor',database='sakila'):
    assert request.method == 'POST' 
    #print(request.get_data())
    a=[]
    a.append(request.get_data())
    a.append(request.form.getlist('Table')[0])
    description=conn.description(appconn,str(request.form.getlist('Table')[0]))
    a.append(description)
    a.append(request.form)
    values=[]
    rows=[]
    
    try:
        for row in description:
            values.append(request.form['Row_'+str(row[0])])
            rows.append(row[0])
    except:
        print('err')
        return
    else:
        value=[rows,values]
        print('value!!!',value)
        conn.Insert(appconn,database,table,value)
        return str(a)

###博客功能
@app.route('/blog/<id>')
def Blog(id=0):
    pass
    return render_template('home.html',info=config.info, name=id)

###微博功能
@app.route('/weibo/<id>')
def Weibo(id=0):
    pass
    return render_template('home.html',info=config.info, name=id)

###启动主程序
if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    #conn.TestConn(app)
    #据说很方便的调试工具，该扩展为 Flask 应用程序添加了一个包含有用的调试信息的工具栏。
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)
    app.run()
    #关闭连接
    conn.Close(appconn)
    #结束程序
    print('Thank you')
