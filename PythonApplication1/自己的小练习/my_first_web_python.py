#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第一个 Flask Web 应用程序
演示 Flask 的基本路由、表单处理和用户认证
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home() -> str:
    """首页路由

    Returns:
        首页 HTML 内容
    """
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form() -> str:
    """登录表单页面路由

    Returns:
        登录表单 HTML 内容
    """
    return '''<form action="/signin" method="post">
              <p>用户名<input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'


@app.route('/signin', methods=['POST'])
def signin() -> str:
    """登录处理路由

    Returns:
        登录结果 HTML 内容
    """
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()