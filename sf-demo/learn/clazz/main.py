#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

from learn.clazz.speaker import speaker
from learn.clazz.student import student
from learn.clazz.vector import vector
from learn.clazz.person import person

# 实例化类
x = person("阿狗", 20)
x.print()
print()
x = speaker("阿狗", 20, "初三")
x.print()
print()
x = student("阿狗", 20, "数学", "初三")
x.print()
print()
# 用子类对象调用父类已被覆盖的方法 多继承调用的是第一个父类
super(student, x).print()
#  重载专有方法
print()
v1 = vector(2, 10)
v2 = vector(5, -2)
print(v1 + v2)
