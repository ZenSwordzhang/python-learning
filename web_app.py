#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/login', methods=['GET'])
def login_form():
    return '''<form action='/login' method='post'>
              <p><input name='username'></p>
              <p><input name='password' type='password'></p>
              <p><button type='submit'>Login</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def login():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == '1234':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password.</h3>'


# 默认请求路径 http://127.0.0.1:5000/
# 登录请求路径 http://127.0.0.1:5000/login
if __name__ == '__main__':
    app.run()
