#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')


def print_array(array):
    '''这是文档字符串'''
    for s in array:
        print(s)
    return array
