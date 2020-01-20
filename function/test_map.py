#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def square(x):
    return x * x


product = map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(product))

str_list = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(str_list)
