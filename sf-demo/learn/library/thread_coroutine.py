#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/19

'''
1. 协程使用生成器函数定义：定义体中有 yield 关键字。
2. yield 在表达式中使用；如果协程只需从客户那里接收数据，那么产出的值是 None —— 这个值是隐式指定的，因为 yield 关键字右边没有表达式。
3. 首先要调用 next(…) 函数，因为生成器还没启动，没在 yield 语句处暂停，所以一开始无法发送数据。
4. 调用send方法，把值传给 yield 的变量，然后协程恢复，继续执行下面的代码，直到运行到下一个 yield 表达式，或者终止。

注意：send方法只有当协程处于 GEN_SUSPENDED 状态下时才会运作，所以我们使用 next() 方法激活协程到 yield 表达式处停止，或者我们也可以使用 sc.send(None)，效果与 next(sc) 一样。
协程的四个状态。当前状态可以使用inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
1. GEN_CREATED：等待开始执行
2. GEN_RUNNING：解释器正在执行
3. GEN_SUSPENED：在yield表达式处暂停
4. GEN_CLOSED：执行结束
'''

def simple_coroutine():
    while True:
        print('-> start')
        x = yield
        print('-> recevied', x)


sc = simple_coroutine()

next(sc)
# sc.send(None)
for i in range(1, 100):
    sc.send('coroutine' + str(i))
