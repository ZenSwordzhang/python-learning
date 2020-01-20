#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


# 创建偏函数
int_2 = functools.partial(int, base=2)


# 默认按十进制转换
print(int('11'))
# 按2进制转换成10进制
print(int_2('11'))
print(int('11', base=2))
# 按8进制转换10进制
print(int('11', base=8))
# 按16进制转换10进制
print(int('11', base=16))




















