#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17


class person:
    """一个简单的类实例"""
    name = "默认"
    age = -1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("我的名字：", self.name)
        print("我的年龄：", self.age)
