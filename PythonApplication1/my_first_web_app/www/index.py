import io
from flask import Flask, render_template, g #, request, session, redirect, url_for, abort
import logging
import config,conn
global app
app = Flask(__name__)

@app.route('/test')
def Test():
    language=conn.Select_language(app,'*')
    return render_template('base.html',info=config.info,language=language.fetchall())

@app.route('/')
@app.route('/<name>')
def Hello(name=None):
    return render_template('home.html',info=config.info, name=name)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    conn.TestConn(app)
    app.run()