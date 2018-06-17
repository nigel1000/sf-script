#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

'''
__private_attrs：两个下划线开头，声明该属性为私有。
__private_method：两个下划线开头，声明该方法为私有方法。
类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
'''


# __add__   重载
class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)
