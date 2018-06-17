#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

class talker():
    content = ''

    def __init__(self, content):
        self.content = content

    # 覆写父类的方法
    def print(self):
        print("演讲内容：", self.content)
