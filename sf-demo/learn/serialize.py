#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

import pickle


def save():
    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4 + 6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    data2 = [1, 2, 3]

    output = open('temp/data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(data2, output, -1)

    output.close()


def load():
    # 使用pickle模块从文件中重构python对象
    pkl_file = open('temp/data.pkl', 'rb')

    data1 = pickle.load(pkl_file)
    print(type(data1))
    print(data1)

    data2 = pickle.load(pkl_file)
    print(type(data2))
    print(data2)

    pkl_file.close()


save()
load()
