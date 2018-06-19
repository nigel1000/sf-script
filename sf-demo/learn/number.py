#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/16

'''
+,-,*,/-浮点数,//-取整-小数点前面的,%-取余-小数点后面的,**-乘方

1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
'''

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))


class A:
    pass


class B(A):
    pass


# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
isinstance(A(), A)  # returns True
print(type(A()) == A)  # returns True
isinstance(B(), A)  # returns True
print(type(B()) == A)  # returns False

# & | ^ ~ << >>
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)
c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", c)
c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", c)
c = ~a  # -61 = 1100 0011
print("4 - c 的值为：", c)
c = a << 2  # 240 = 1111 0000
print("5 - c 的值为：", c)
c = a >> 2  # 15 = 0000 1111
print("6 - c 的值为：", c)

a = 10
b = 20

# and or not
if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")
# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")
if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")
