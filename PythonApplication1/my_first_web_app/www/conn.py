# MySql conn
import pymysql
import logging

def log(sql, args=()):
    logging.info('SQL: %s' % sql)
    return

def TestConn():
    conn = Conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM language")
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logging.info(cur.description)
    logging.info(cur.fetchall())
    Close(conn)
    return

def Conn():
    log('create database connection pool...')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sakila')
    return conn

def Close(conn):
    conn.cursor()
    conn.close()
    return

if __name__ == '__main__':
    TestConn()

