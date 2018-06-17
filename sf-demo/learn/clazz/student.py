#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

from learn.clazz.person import person
from learn.clazz.talker import talker


# 多继承示例
class student(talker, person):
    grade = ''

    def __init__(self, name, age, content, grade):
        # 调用父类的构函
        person.__init__(self, name, age)
        talker.__init__(self, content)
        self.grade = grade

    # 覆写父类的方法
    def print(self):
        person.print(self)
        talker.print(self)
        print("我的年级：", self.grade)
