#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from _datetime import datetime
import functools


def now():
    print(datetime.now())


def log_1(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# log_1方法要先于now_1方法定义，如果把log_1放于now_1后面，会提示编译错误
@log_1
def now_1():
    print(datetime.now())


def log_2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_2('execute')
def now_2():
    print(datetime.now())


def log_3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 不带参数
@log_3
def now_3():
    print(datetime.now())


# 带参数
def log_4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_4('execute')
def now_4():
    print(datetime.now())


f = now
f()
print(now.__name__)
print(f.__name__)

f1 = now_1
f1()
print(now_1.__name__)
print(f1.__name__)

now_2()
print(now_2.__name__)

now_3()
print(now_3.__name__)

now_4()
print(now_4.__name__)
