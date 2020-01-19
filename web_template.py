#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
    return render_template('form.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1234':
        return render_template('login_ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


# 默认请求路径 http://127.0.0.1:5000/
# 登录请求路径 http://127.0.0.1:5000/login
# pip3 install jinja2


if __name__ == '__main__':
    app.run()
