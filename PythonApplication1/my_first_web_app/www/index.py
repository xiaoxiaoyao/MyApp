import io
from flask import Flask, render_template, g #, request, session, redirect, url_for, abort
import config

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('base.html',info=config.info)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('home.html',info=config.info, name=name)

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.run()