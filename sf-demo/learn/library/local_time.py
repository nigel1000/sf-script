#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

import time
import calendar
from calendar import Calendar

# http://www.runoob.com/python3/python3-date-time.html

# 时间操作
localtime = time.localtime(time.time())
print("本地时间为 :", time.asctime(localtime))
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", localtime))
# 将格式字符串转换为时间戳
print(time.mktime(time.strptime("Sat Mar 28 22:24:24 2016", "%a %b %d %H:%M:%S %Y")))

# 日历操作
print()
cal_str = calendar.month(2018, 6)
print("以下输出2018年6月份的日历:\n", cal_str)
cal = Calendar()
print(",".join([str(v) for v in cal.iterweekdays()]))
# 是否闰年
print()
print(calendar.isleap(2018))
