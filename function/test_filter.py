#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def not_blank(str_1):
    return str_1 and str_1.strip()


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    # 初始序列
    it = odd_iter()
    while True:
        # 返回序列的第一个数
        n = next(it)
        yield n
        # 构造新序列
        it = filter(not_divisible(n), it)


even_ = list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(even_)
odd_ = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(odd_)
str_ = list(filter(not_blank, ['1', '', ' ', '3', None, '5', '  ']))
print(str_)
# 打印1000以内的素数:
for m in primes():
    if m < 1000:
        print(m)
    else:
        break
