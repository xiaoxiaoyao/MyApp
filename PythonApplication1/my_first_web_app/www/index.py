# -*- coding: utf-8 -*-
import io
from flask import Flask, render_template, g , request, url_for, session, redirect, abort
import config,conn
global app
###初始化程序
app = Flask(__name__)
###初始化数据链接
appconn=conn.Conn(app)

###测试模块
@app.route('/test', methods=("GET", "POST"))
def Test():
    cur=conn.Select_table(appconn,'*')
    return render_template('base.html',info=config.info,language=cur.fetchall())

###首页
@app.route('/')
@app.route('/<name>')
def Index(name=None):
    return render_template('home.html',info=config.info, name=name)

###数据库演示页和跳转页
@app.route('/database/<database>')
def Databasegoto(database=None):
    return redirect(url_for('Database',database='sakila', table='actor'))
@app.route('/database/<database>/<table>',methods=("GET", "POST"))
def Database(table='actor',database='sakila'):
    row=request.args.get('row', '*')
    cur=conn.Select_table(appconn,row,table)
    tables=conn.Show_tables(appconn)
    pass
    return render_template('database.html',info=config.info, data=cur,database=database,table=table,tables=tables,row=row)
#@app.route('/database/<database>/<table>',methods="POST")
#def Data123123123(table='actor',database='sakila'):
    #return ""

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
    app.run()
    conn.Close(appconn)
    print('Thank you')
