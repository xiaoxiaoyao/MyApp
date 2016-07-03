# MySql conn
'''
数据库链接，Conn(app)返回数据库连接conn，cur = conn.cursor()，SQL语句放在cur.execute(SQL语句)里面，cur.description是表头，cur.fetchall()是返回的所有内容。
'''
__author__ = 'lai yao (lake.lai)'
import pymysql
import logging
##为了方便，把index.py app = Flask(__name__)变成coon.py的全局变量
global app

def TestConn(app):
    logging.basicConfig(level = logging.INFO)#开始测试就修改日志(level = logging.INFO)
    app.logger.info("next is app and appconn")
    app.logger.info(app)
    app.logger.info(appconn)
    conn = Conn(app)
    cur = conn.cursor()
    app.logger.info("cur.execute(sql) SQL:SELECT * FROM language")
    cur.execute("SELECT * FROM language")
    app.logger.debug(cur.description)
    app.logger.debug(cur.fetchall())
    Close(conn)
    return

def Conn(app_):
    global app
    app=app_
    app.logger.info(app)
    app.logger.info('create database connection pool...正在建立数据库连接......')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sakila')
    app.logger.info(conn)
    return conn

def Select_table(conn,name='*',table='actor'):
    cur = conn.cursor()
    sql="SELECT "+ name +" FROM " + table
    app.logger.info("cur.execute(sql) SQL:" + sql)
    cur.execute(sql)
    return cur

def Insert(conn,database,table,values=[[],[]]):
    cur = conn.cursor()
    values1_table_name=[]
    values2_VALUES=[]
    i=0
    for item in values[1]:
        if(item != ''):#去掉空内容
            values1_table_name.append(values[0][i])
            values2_VALUES.append(values[1][i])
        i=i+1
    a=","
    values1_table_name=a.join(values1_table_name)
    sql="INSERT INTO " + database+"."+table +" (" + str(values1_table_name) + ") VALUES "+ str(tuple(values2_VALUES)) +";"
    app.logger.info("cur.execute(sql) SQL:" + sql)
    try:
        cur.execute(sql)
    except cur.connection.ProgrammingError as err:
        app.logger.info(err)
        return []
    finally:
        app.logger.info("finally",cur.description)
    return 

def description(conn,table='actor'):
    cur = conn.cursor()
    sql="SELECT * FROM " + table + " WHERE FALSE"
    app.logger.info("cur.execute(sql) SQL:" + sql)
    try:
        cur.execute(sql)
    except cur.connection.ProgrammingError as err:
        app.logger.info(err)
        return []
    except:
        app.logger.info('error')
        return []
    finally:
        return cur.description

def delect(conn,table,values):
    cur = conn.cursor()
    app.logger.info("cur.execute(sql) SQL:" + sql)
    pass

def Show_tables(conn):
    cur = conn.cursor()
    sql="show tables"
    app.logger.info("cur.execute(sql) SQL:" + sql)
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

