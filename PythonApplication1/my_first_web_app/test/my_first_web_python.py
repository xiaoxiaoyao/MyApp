# -*- coding: utf-8 -*-
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
from flask import Flask, render_template,request
import time,os,sched,threading
import 基础配置

app = Flask(__name__)

员工1=基础配置.员工()
员工2=基础配置.员工()
门店=基础配置.门店(门店名字="123初始门店店",初始资金=0,员工=[员工1,员工2],客户=[],环境="这一项还在开发中")


@app.route('/', methods=['GET','POST'])
def home(info=""):
    return render_template('fin.html',门店=门店,info=info)


@app.route('/addHamburg', methods=['POST'])
def a():
    return home(info=基础配置.加汉堡(门店=门店))

@app.route('/addShopper', methods=['POST'])
def b():
    return home(info=基础配置.加顾客(门店=门店,消费金额=25))

@app.route('/addPersonnel', methods=['POST'])
def c():
    return home(info=基础配置.加员工(门店=门店,员工名字="门店员工") )

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>啦啦啦<input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

#其中 if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')#即可全网使用
    #app.run(debug=True)#即可调试模式，允许网页执行任意代码
