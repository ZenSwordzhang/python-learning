#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
import unittest


class DateTimeTest(unittest.TestCase):

    def test_datetime(self):

        # 获取当前时间
        now = datetime.now()
        # 如果仅导入import datetime，则必须引用全名datetime.datetime
        # 通过from datetime import datetime导入的才是datetime这个类
        self.assertTrue(type(now) is datetime)

        # 设置指定时间
        dt = datetime(2020, 3, 16, 11, 20, 11)
        self.assertEqual('2020-03-16 11:20:11', str(dt))

        # datetime转换为timestamp
        self.assertEqual(1584328811.0, dt.timestamp())

        # timestamp转换为datetime
        timestamp_1 = 1584328812.0
        self.assertEqual(datetime(2020, 3, 16, 11, 20, 12), datetime.fromtimestamp(timestamp_1))
        # UTC标准时区的时间
        self.assertEqual(datetime(2020, 3, 16, 3, 20, 12), datetime.utcfromtimestamp(timestamp_1))

        # str转换为datetime
        dt_1 = datetime.strptime('2020-3-16 11:20:11', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(2020, dt_1.year)
        self.assertEqual(3, dt_1.month)
        self.assertEqual(16, dt_1.day)
        self.assertEqual(11, dt_1.hour)
        self.assertEqual(20, dt_1.minute)
        self.assertEqual(11, dt_1.second)

        # datetime转换为str
        self.assertEqual('Mon, Mar 16 11:20', dt_1.strftime('%a, %b %d %H:%M'))

        # datetime加减
        dt_2 = dt_1 + timedelta(hours=10)
        self.assertEqual(2020, dt_2.year)
        self.assertEqual(3, dt_2.month)
        self.assertEqual(16, dt_2.day)
        self.assertEqual(21, dt_2.hour)
        self.assertEqual(20, dt_2.minute)
        self.assertEqual(11, dt_2.second)

        dt_3 = dt_1 - timedelta(days=10)
        self.assertEqual(2020, dt_3.year)
        self.assertEqual(3, dt_3.month)
        self.assertEqual(6, dt_3.day)
        self.assertEqual(11, dt_3.hour)
        self.assertEqual(20, dt_3.minute)
        self.assertEqual(11, dt_3.second)

        dt_4 = dt_1 + timedelta(days=2, hours=3)
        self.assertEqual(2020, dt_4.year)
        self.assertEqual(3, dt_4.month)
        self.assertEqual(18, dt_4.day)
        self.assertEqual(14, dt_4.hour)
        self.assertEqual(20, dt_4.minute)
        self.assertEqual(11, dt_4.second)

        # 本地时间转换为UTC时间
        utc_dt_1 = dt_1.replace(tzinfo=timezone.utc)
        print(utc_dt_1)






if __name__ == '__main__':
    unittest.main()