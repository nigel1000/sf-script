#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17
import json

# 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
print()
data2 = json.loads(json_str)
print(data2)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# 写入 JSON 数据
print()
with open('../temp/data.json', 'w') as f:
    json.dump(data, f)
# 读取数据
with open('../temp/data.json', 'r') as f:
    data = json.load(f)
    print(data)
