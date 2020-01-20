#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


# 将字符串转成数字
def char_num1(key):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[key]


# 将字符串转成数字
def str2int(str_):

    def fn1(x, y):
        return x * 10 + y

    def char_num2(key1):
        return DIGITS[key1]

    return reduce(fn1, map(char_num2, str_))


def char_num2(key):
    return DIGITS[key]


# 将字符串转成数字
def str_int2(str_):
    return reduce(lambda x, y: x * 10 + y, map(char_num2, str_))


sum_ = reduce(add, [1, 3, 5, 7, 9])
print(sum_)

product_sum = reduce(fn, [1, 3, 5, 7, 9])
print(product_sum)

m_int = reduce(fn, map(char_num1, '24680'))
print(m_int)

m_ = str2int('12345')
print(m_)

m_1 = str2int('45678')
print(m_1)