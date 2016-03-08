# MySql conn
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
    app.logger.info('create database connection pool...')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sakila')
    return conn

def Select_table(conn,name='*',table='actor'):
    cur = conn.cursor()
    sql="SELECT "+ name +" FROM " + table
    cur.execute(sql)
    return cur

def Select_language(conn,name='*'):
    cur = conn.cursor()
    sql="SELECT * FROM language"
    cur.execute(sql)
    return cur

def Close(conn):
    conn.cursor()
    conn.close()
    return

if __name__ == '__main__':
    TestConn(app)

