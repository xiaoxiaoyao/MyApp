# MySql conn
'''
数据库链接，Conn(app)返回数据库连接conn，cur = conn.cursor()，SQL语句放在cur.execute(SQL语句)里面，cur.description是表头，cur.fetchall()是返回的所有内容。
'''
__author__ = 'lai yao (lake.lai)'
import pymysql

def TestConn(app):
    conn = Conn(app)
    cur = conn.cursor()
    cur.execute("SELECT * FROM language")
    app.logger.debug(cur.description)
    app.logger.debug(cur.fetchall())
    Close(conn)
    return

def Conn(app):
    app.logger.info('create database connection pool...正在建立数据库连接......')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sakila')
    return conn

def Select_table(conn,name='*',table='actor'):
    cur = conn.cursor()
    sql="SELECT "+ name +" FROM " + table
    cur.execute(sql)
    return cur

def Insert(conn,table,values):
    pass

def description(conn,table='actor'):
    cur = conn.cursor()
    sql="SELECT * FROM " + table + " WHERE FALSE"
    cur.execute(sql)
    return cur.description

def delect(conn,table,values):
    pass

def Show_tables(conn):
    cur = conn.cursor()
    sql="show tables"
    cur.execute(sql)
    return cur

def Close(conn):
    conn.cursor()
    conn.close()
    return

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    TestConn(app)

