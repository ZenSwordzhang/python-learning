#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import unittest


class StudyTest(unittest.TestCase):

    def modify_tuple(self, tup_1):
        # 元组中的元素值是不允许修改
        tup_1[0] = 100

    def test_get_current_work_dir(self):
        print(os.getcwd())
        self.assertEqual(1, 1)

    def test_list(self):
        # 创建一个列表
        list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(6, len(list_1))
        # 访问列表中的值
        self.assertEqual('a', list_1[0])
        # 更新列表
        list_1[0] = 1
        self.assertEqual(1, list_1[0])
        # 删除列表元素
        del list_1[0]
        self.assertEqual('b', list_1[0])
        self.assertEqual(5, len(list_1))
        # 嵌套列表
        list_2 = [1, 2, 3, 5]
        list_3 = [list_2, list_1, 5, 6]
        self.assertEqual(4, len(list_3))
        self.assertEqual(1, list_3[0][0])
        # 在列表的第三个位置插入数据
        list_2.insert(3, 4)
        # 在列表的指定位置插入数据，如果指定位置大于列表的长度，数据会插入到列表的末尾
        list_2.insert(7, 6)
        self.assertEqual(6, list_2[5])
        # 修改嵌套列表list_3中的列表list_2元素，相应的list_3也会改变
        self.assertEqual(6, list_3[0][5])
        # 追加数据到列表
        list_1.append('b')
        self.assertEqual(6, len(list_1))
        self.assertEqual('b', list_1[5])
        # 统计元素'b'在列表中出现的次数
        self.assertEqual(2, list_1.count('b'))
        list_4 = ['A', 'B', 'C']
        # 在列表末尾一次性追加另一个列表的值
        list_1.extend(list_4)
        self.assertEqual(9, len(list_1))
        self.assertEqual('C', list_1[8])
        # 从列表中找出'c'第一个匹配项的索引位置
        self.assertEqual(1, list_1.index('c'))
        # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        str_1 = list_4.pop()
        self.assertEqual(2, len(list_4))
        self.assertEqual('C', str_1)
        str_2 = list_4.pop(0)
        self.assertEqual(1, len(list_4))
        self.assertEqual('A', str_2)
        # 移除列表中某个值的第一个匹配项
        list_5 = ['A', 'B', 'C', 'A', 'B', 'C']
        list_5.remove('B')
        self.assertEqual(5, len(list_5))
        self.assertEqual('C', list_5[1])
        # 反向列表中元素
        list_5.reverse()
        self.assertEqual('C', list_5[0])

    def test_tuple(self):
        # 创建空元组
        tup_0 = ()
        self.assertIsNotNone(tup_0)
        self.assertEqual(0, len(tup_0))
        # 使用小括号
        tup_1 = ('1', '2', 3, 4, 5, 6)
        # 不适用括号
        tup_2 = 'a', 'b', 'c', 'd', 'e', 'f'
        # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
        tup_3 = (3)
        self.assertTrue(type(tup_3) is int)
        tup_4 = (3,)
        self.assertTrue(type(tup_4) is tuple)
        # 获取元组中单个元素
        self.assertEqual('1', tup_1[0])
        self.assertRaisesRegex(IndexError, "tuple index out of range", tup_1.__getitem__, 6)
        # 获取元组中多个元素（包头不包尾）
        var = tup_2[1:4]
        self.assertIsInstance(var, tuple)
        self.assertTupleEqual(('b', 'c', 'd'), var)
        # 修改元组（元组中的元素值是不允许修改）
        self.assertRaisesRegex(TypeError, "'tuple' object does not support item assignment", self.modify_tuple, tup_2)
        # 创建一个新的元组
        tup_5 = tup_1 + tup_2 + tup_4
        self.assertEqual(13, len(tup_5))
        # 删除元组
        del tup_5

    # d = {key1 : value1, key2 : value2 }
    def test_dict(self):
        # 创建一个空字典
        dict_0 = {}
        self.assertEqual(0, len(dict_0))
        # 创建字典
        dict_1 = {'name': 'zhangsan', 'age': '11', 'gender': 'male'}
        # 字典元素个数
        self.assertEqual(3, len(dict_1))
        # 将字典转成字符串
        self.assertEqual("{'name': 'zhangsan', 'age': '11', 'gender': 'male'}", str(dict_1))
        # 键值存在
        self.assertEqual("zhangsan", dict_1['name'])
        # 比较数据类型
        self.assertTrue(type(dict_1) is dict)
        # 键值不存在，会报异常
        with self.assertRaisesRegex(KeyError, 'name1'):
            var = dict_1['name1']
            print(var)
        # 判断键值是否存在
        self.assertFalse('name1' in dict_1.keys())
        # 修改键值
        dict_1['age'] = 18
        self.assertEqual(18, dict_1['age'])
        # 删除键
        del dict_1['gender']
        self.assertRaisesRegex(KeyError, 'gender', dict_1.__getitem__, 'gender')
        # 清空字典
        dict_1.clear()
        self.assertRaisesRegex(KeyError, 'name', dict_1.__getitem__, 'name')
        # 删除字典
        del dict_1

    def test_set(self):
        # 创建一个空集合
        set_0 = set()
        self.assertEqual(0, len(set_0))
        # 创建集合
        set_1 = set('abcdef')
        self.assertEqual(6, len(set_1))
        set_2 = {'a', 'b', 'c', 'A', 'B', 'C'}
        self.assertEqual(6, len(set_2))
        # 判断元素是否在集合内
        self.assertTrue('a' in set_1)
        # 向集合中添加元素
        set_1.add('g')
        self.assertTrue('g' in set_1)

        # 包含在集合set_1但不包含在set_2的中元素
        set_3 = set_1 - set_2
        self.assertEqual(4, len(set_3))
        self.assertFalse('a' in set_3)
        self.assertTrue('d' in set_3)
        self.assertFalse('A' in set_3)

        # 包含在集合set_1或set_2中的所有元素
        set_4 = set_1 | set_2
        self.assertEqual(10, len(set_4))
        self.assertTrue('a' in set_4)
        self.assertTrue('d' in set_4)
        self.assertTrue('A' in set_4)

        # 同时包含在set_1和set_2的元素
        set_5 = set_1 & set_2
        self.assertEqual(3, len(set_5))
        self.assertTrue('a' in set_5)
        self.assertFalse('d' in set_5)
        self.assertFalse('A' in set_5)

        # 同时都不包含于set_1和set_2的元素
        set_6 = set_1 ^ set_2
        self.assertEqual(7, len(set_6))
        self.assertFalse('a' in set_6)
        self.assertTrue('d' in set_6)
        self.assertTrue('A' in set_6)

        set_7 = {'A', 'B', 'C'}
        # 向集合中添加元素，参数是列表
        # {'A', 'B', 'C', '2', '1'}
        set_7.update(['1', '2'])
        self.assertEqual(5, len(set_7))
        self.assertTrue('1' in set_7)

        # 向集合中添加元素，参数是元组
        # {'A', '1', 'a', '2', 'B', 'C', 'b'}
        set_7.update(('a', 'b'))
        self.assertEqual(7, len(set_7))
        self.assertTrue('a' in set_7)

        # 向集合中添加元素，参数是字典
        # {'C', 'b', 'A', '1', 'age', 'a', '2', 'B'}
        set_7.update({'age': 18})
        self.assertEqual(8, len(set_7))
        self.assertTrue('age' in set_7)

        # 移除元素
        # {'A', '1', 'a', '2', 'B', 'C', 'b'}
        set_7.remove('age')
        self.assertEqual(7, len(set_7))
        self.assertFalse('age' in set_7)
        # 移除元素，元素不存在报错
        self.assertRaisesRegex(KeyError, "age", set_7.remove, 'age')
        set_7.discard('b')
        self.assertEqual(6, len(set_7))
        self.assertFalse('b' in set_7)
        # 移除元素，元素不存在不报错
        set_7.discard('b')
        # 随机删除集合中的一个元素，并返回该元素
        str_1 = set_7.pop()
        self.assertEqual(5, len(set_7))
        self.assertFalse(str_1 in set_7)
        set_8 = {'a', 'b'}
        # 复制一个集合
        set_9 = set_8.copy()
        self.assertEqual(set_8, set_9)
        set_10 = {'a', 'A', 'B'}

        # 包含于set_8，但不包含于set_10
        # set_8 - set_10
        # {'b'}
        set_11 = set_8.difference(set_10)
        self.assertEqual(1, len(set_11))
        self.assertFalse('a' in set_11)
        self.assertTrue('b' in set_11)
        self.assertFalse('A' in set_11)

        # 包含在集合set_1或set_2中的所有元素
        # set_8 | set_10
        # {'b', 'a', 'A', 'B'}
        set_12 = set_8.union(set_10)
        self.assertEqual(4, len(set_12))
        self.assertTrue('a' in set_12)
        self.assertTrue('b' in set_12)
        self.assertTrue('A' in set_12)

        # 同时包含在set_1和set_2的元素
        # set_8 & set_10
        # {'a'}
        set_13 = set_8.intersection(set_10)
        self.assertEqual(1, len(set_13))
        self.assertTrue('a' in set_13)
        self.assertFalse('b' in set_13)
        self.assertFalse('A' in set_13)

        # 同时都不包含于set_1和set_2的元素
        # set_8 ^ set_10
        # 'b', 'A', 'B'}
        set_14 = set_8.symmetric_difference(set_10)
        self.assertEqual(3, len(set_14))
        self.assertFalse('a' in set_14)
        self.assertTrue('b' in set_14)
        self.assertTrue('A' in set_14)




    def test_exception(self):
        self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
        with self.assertRaisesRegex(ValueError, "invalid"):
            int('XYZ')


if __name__ == '__main__':
    unittest.main()
