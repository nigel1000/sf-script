#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

from learn.clazz.person import person


# 单继承示例
class speaker(person):
    content = ''

    def __init__(self, name, age, content):
        # 调用父类的构函
        person.__init__(self, name, age)
        self.content = content

    # 覆写父类的方法
    def print(self):
        person.print(self)
        print("演讲内容：", self.content)
