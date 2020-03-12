#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import unittest


class StudyTest(unittest.TestCase):

    def test_get_current_work_dir(self):
        print(os.getcwd())
        self.assertEqual(1, 1)

    def test_tup(self):
        # 创建空元组
        tup_0 = ()
        self.assertIsNotNone(tup_0)
        self.assertEqual(0, len(tup_0))
        # 使用小括号
        tup_1 = ('1', '2', 3, 4, 5, 6)
        # 不适用括号
        tup_2 = 'a', 'b', 'c', 'd', 'e', 'f'
        # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
        tup_3 = (1)
        self.assertTrue(type(tup_3) is int)
        tup_4 = (1,)
        self.assertTrue(type(tup_4) is tuple)
        # 获取元组中单个元素
        self.assertEqual('1', tup_1[0])
        self.assertRaisesRegex(IndexError, "tuple index out of range", tup_1.__getitem__, 6)
        # 获取元组中多个元素（包头不包尾）
        var = tup_2[1:4]
        self.assertIsInstance(var, tuple)
        self.assertTupleEqual(('b', 'c', 'd'), var)
        # 修改元组（元组中的元素值是不允许修改）




    # d = {key1 : value1, key2 : value2 }
    def test_dict(self):
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
            dict_1['name1']
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

    def test_exception(self):
        self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
        with self.assertRaisesRegex(ValueError, "invalid"):
            int('XYZ')


if __name__ == '__main__':
    unittest.main()
