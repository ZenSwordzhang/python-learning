#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

fn_1 = lambda x: x * x
print(fn_1)
print(fn_1(5))


def sum_square(x1, y1):
    return (lambda x, y: x * x + y * y)(x1, y1)


sum_ = sum_square(5, 6)
print(sum_)
