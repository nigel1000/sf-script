#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

import re

# http://www.runoob.com/python3/python3-reg-expressions.html
line = "Cats are smarter than dogs"

# re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
# re.search(pattern, string, flags=0)
# re.search 扫描整个字符串并返回第一个成功的匹配。
print()
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None。
# re.search匹配整个字符串，直到找到一个匹配。
print()
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
# 检索和替换
# re.sub(pattern, repl, string, count=0)
# 参数：
#     pattern : 正则中的模式字符串。
#     repl : 替换的字符串，也可为一个函数。
#     string : 要被查找替换的原始字符串。
#     count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
print()
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
s = 'A23G4HFD567'
# 将匹配的数字乘于 2
double = lambda matched: str(int(matched.group('value')) * 2)
print(re.sub('(?P<value>\d+)', double, s))

# findall(string[, pos[, endpos]])
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
print()
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
# re.finditer(pattern, string, flags=0)
# 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
