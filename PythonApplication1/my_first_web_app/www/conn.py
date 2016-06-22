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

def Insert(conn,database,table,values=[[],[]]):
    cur = conn.cursor()
    values1_table_name=[]
    values2_VALUES=[]
    i=0
    for item in values[1]:
        if(item != ''):
            values1_table_name.append(values[0][i])
            values2_VALUES.append(values[1][i])
        i=i+1
    a=","
    values1_table_name=a.join(values1_table_name)
    sql="INSERT INTO " + database+"."+table +" (" + str(values1_table_name) + ") VALUES "+ str(tuple(values2_VALUES)) +";"
    print("SQL:",sql)
    try:
        cur.execute(sql)
    except cur.connection.ProgrammingError as err:
        print(err)
        return []
    finally:
        print("finally",cur.description)
    return 

def description(conn,table='actor'):
    cur = conn.cursor()
    sql="SELECT * FROM " + table + " WHERE FALSE"
    try:
        cur.execute(sql)
    except cur.connection.ProgrammingError as err:
        print(err)
        return []
    except:
        print('error')
        return []
    finally:
        return cur.description

def delect(conn,table,values):
    cur = conn.cursor()
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

