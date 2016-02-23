# MySql conn test
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sakila')
cur = conn.cursor()
cur.execute("SELECT * FROM actor")
print(cur.description)
print(cur.fetchall())
cur.close()
conn.close()