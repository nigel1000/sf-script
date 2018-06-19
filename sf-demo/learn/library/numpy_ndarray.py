#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/19

import numpy as np

'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
上面的构造器接受以下参数：
    object 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列。
    dtype 数组的所需数据类型，可选。
    copy 可选，默认为true，对象是否被复制。
    order C（按行）、F（按列）或A（任意，默认）。
    subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
    ndmin 指定返回数组的最小维数。
itemsize 返回数组中每个元素的字节单位长度
'''

a = np.array([[1, 2], [3, 4]])
print(a)

print()
a = np.array([1, 2, 3, 4, 5], ndmin=3)
print(a)

print()
a = np.array([1, 2, 3], dtype=complex)
print(a)

# i1->int 1,f4->2的4次方
#   'b'：布尔值
#   'i'：符号整数
#   'u'：无符号整数
#   'f'：浮点
#   'c'：复数浮点
#   'm'：时间间隔
#   'M'：日期时间
#   'O'：Python 对象
#   'S', 'a'：字节串
#   'U'：Unicode
#   'V'：原始数据（void）
print()
student = np.dtype([('name', 'S10'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)

# 调整数组大小
print()
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(a)
a.shape = (3, 2)
print(a)
print(a.reshape(1, 6))

print()
# 一维数组
a = np.arange(24)
print(a.ndim)
# 现在调整其大小
b = a.reshape(2, 4, 3)
# b 现在拥有三个维度
print(b)

# ndarray对象拥有以下属性。这个函数返回了它们的当前值。
#     C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
#     F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
#     OWNDATA (O) 数组的内存从其它对象处借用
#     WRITEABLE (W) 数据区域可写入。 将它设置为false会锁定数据，使其只读
#     ALIGNED (A) 数据和任何元素会为硬件适当对齐
#     UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新
print()
x = np.array([1, 2, 3, 4, 5])
print(x.flags)

print()
x = np.empty([3, 2], dtype=int)
print(x)
# 以 0 填充的新数组
x = np.zeros([3, 2], dtype=int)
print(x)
# 以 1 填充的新数组
x = np.ones([3, 2], dtype=int)
print(x)
