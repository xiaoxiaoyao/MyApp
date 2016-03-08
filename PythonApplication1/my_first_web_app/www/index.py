import io
from flask import Flask, render_template, g , request, url_for, session, redirect, abort
import logging
import config,conn
global app
app = Flask(__name__)
appconn=conn.Conn(app)

@app.route('/test')
def Test():
    cur=conn.Select_language(appconn,'*')
    return render_template('base.html',info=config.info,language=cur.fetchall())

@app.route('/')
@app.route('/<name>')
def Hello(name=None):
    return render_template('home.html',info=config.info, name=name)

@app.route('/database/<database>')
def Databasegoto(database=None):
    return redirect(url_for('Database',database='sakila', table='actor'))

@app.route('/database/<database>/<table>')
def Database(table='actor',database='sakila'):
    row=request.args.get('row', '*')
    cur=conn.Select_table(appconn,row,table)
    pass
    return render_template('database.html',info=config.info, data=cur,database=database,table=table,row=row)

@app.route('/blog/<id>')
def Blog(id=0):
    pass
    return render_template('home.html',info=config.info, name=id)

@app.route('/weibo/<id>')
def Weibo(id=0):
    pass
    return render_template('home.html',info=config.info, name=id)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    #conn.TestConn(app)
    app.run()
    print('Thank you')
