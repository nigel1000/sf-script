#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/16

'''
创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# 输出集合，重复的元素被自动去掉
print(student)

# set可以进行集合运算
a = set('asdfghj')
b = set('ghjklouyhh')
print(a)  # {'g', 'h', 'f', 'a', 'd', 's', 'j'}
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
