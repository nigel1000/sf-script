#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/16

import keyword
import sys

# 数据类型
'''
六个标准的数据类型：
    Number（数字） +,-,*,/-浮点数,//-取整,%-取余,**-乘方
         int
         float
         bool
         complex（复数）
    String（字符串）
    List（列表）    []
    Tuple（元组）   ()
    Sets（集合）    set()&{}
    Dictionary（字典）  {}
不可变数据（四个）：Number（数字）、String（字符串）、Tuple（元组）、Sets（集合）；
可变数据（两个）：List（列表）、Dictionary（字典）。
'''
# 类型转换
'''
int(x [,base])  将x转换为一个整数
float(x)    将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)  将对象 x 转换为字符串
repr(x) 将对象 x 转换为表达式字符串
eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)    将序列 s 转换为一个元组
list(s) 将序列 s 转换为一个列表
set(s)  转换为可变集合
dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)    转换为不可变集合
chr(x)  将一个整数转换为一个字符
ord(x)  将一个字符转换为它的整数值
hex(x)  将一个整数转换为一个十六进制字符串
oct(x)  将一个整数转换为一个八进制字符串
'''
# is&==区别
'''
is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
# 逻辑语法
'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

while 判断条件：
    语句

while 判断条件：
    语句
else:  
    语句

for <variable> in <sequence>:
    <statements>
else:
    <statements>      
'''
# 函数定义
'''
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域。
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
global  修改全局变量
nonlocal    修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量
# global 示例
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
# nonlocal 示例
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

以下是调用函数时可使用的正式参数类型：
1.必需参数
    def func( str ):
2.关键字参数
    def func( name, age ):
    func( age=50, name="test" )
3.默认参数
    def func( name, age = 35 ):
4.不定长参数
    def func( arg1, *tuple ):
    func( 70, 60, 50 )
    def func( arg1, **dict ):
    func(1, a=2,b=3)
5.匿名函数lambda 
    sum = lambda arg1, arg2: arg1 + arg2  
    print ("相加后的值为 : ", sum( 10, 20 ))
'''
# 列表推导式
'''
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
如果希望表达式推导出一个元组，就必须使用括号。
>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]
'''
# 遍历技巧
'''
字典中遍历:  for k, v in dict.items():
索引位置和对应值:   for i, v in enumerate(['tic', 'tac', 'toe']):
同时遍历两个或更多的序列:   for q, a in zip(questions, answers):
'''
# 文件操作
''' http://www.runoob.com/python3/python3-file-methods.html
打开文件的模式：只读r，写入w，追加a。
f.read()｜f.readline()｜f.readlines()｜f.close()｜f.write()｜f.tell()｜f.seek()
f = open("/tmp/foo.txt", "r")
for line in f:
    print(line, end='')
f.close()
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。
with open('/tmp/foo.txt', 'r') as f:
    read_data = f.read()
'''
# 文件/目录方法
''' http://www.runoob.com/python3/python3-os-file-methods.html
执行系统命令  os.system('mkdir today') 
改变当前工作目录    os.chdir(path)
返回当前工作目录    os.getcwd()
返回path指定的文件夹包含的文件或文件夹的名字的列表 os.listdir(path)
以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。   os.mkdir(path[, mode])
删除路径为path的文件。如果path 是一个文件夹，将抛出OSError。  os.remove(path)
删除path指定的空目录，如果目录非空，则抛出一个OSError异常。 os.rmdir(path)
递归删除目录。 os.removedirs(path)
创建硬链接，名为参数dst，指向参数src   os.link(src, dst)
创建一个软链接 os.symlink(src, dst)
重命名文件或目录，从src到dst。    os.rename(src, dst)
通配符搜索文件列表   glob.glob('*.py')
复制文件    shutil.copyfile('data.db', 'archive.db')
移动文件    shutil.move('/build/executables', 'installdir')
关闭文件描述符 fd  os.close(fd)  fd＝open(path).fileno()｜fd = os.open(path)
'''
# 错误和异常
'''
Python有两种错误很容易辨认：语法错误和异常。
try:
    pass
except (RuntimeError, TypeError, NameError):
    pass
except:
    raise
else:
    pass
finally:
    raise
try语句按照如下方式工作：
    首先，执行try子句（在关键字try和关键字except之间的语句）
    如果没有异常发生，忽略except子句，try子句执行后结束。
    如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。
    如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
    如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
    一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
    else子句将在try子句没有发生任何异常的时候执行。
'''
# 网络编程
'''
协议	    功能用处    端口号	Python 模块
HTTP	    网页访问    80	    httplib, urllib, xmlrpclib
FTP	    文件传输    20	    ftplib, urllib
SMTP	    发送邮件    25	    smtplib
POP3	    接收邮件    110	    poplib
IMAP4	    获取邮件    143	    imaplib
Telnet	命令执行    23	    telnetlib
Gopher	信息查找    70	    gopherlib, urllib
'''

from learn.module import module1

# 输出函数的注释
print()
print(module1.print_array.__doc__)

# 查看py的系统保留关键字
print()
print('系统保留关键字:')
module1.print_array(keyword.kwlist)

# 查看命令行参数
print()
print('命令行参数为:')
for i in sys.argv:
    print(i)
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
print('python 路径:', sys.path)
