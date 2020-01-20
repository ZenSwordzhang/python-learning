#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从小到大排序
list_ = sorted([5, 15, -10, 9, -20])
print(list_)
# 按绝对值从小到大排序
list_ = sorted([5, 15, -10, 9, -20], key=abs)
print(list_)
list_ = sorted(['t', 'c', 'G', 'A', 'a', 'T', 'M'])
print(list_)
list_ = sorted(['Ja', 'ja', 'Java', 'C#', 'C', 'C++', 'c++', 'python'])
print(list_)
# 忽略大小写
list_ = sorted(['Ja', 'ja', 'Java', 'C#', 'C', 'C++', 'c++', 'python'], key=str.lower)
print(list_)
# 反向排序
list_ = sorted(['Ja', 'ja', 'Java', 'C#', 'C', 'C++', 'c++', 'python'], reverse=True)
print(list_)