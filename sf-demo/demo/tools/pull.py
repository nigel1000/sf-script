#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/13

import sys
import os


def pullPath(path):
    files = os.listdir(path)
    for f in files:
        filePath = path + '/' + f
        if (os.path.isdir(filePath)):
            if (f == ".git"):
                curr_dir = os.getcwd()
                os.chdir(path)
                command = "git pull "
                print(command + path)
                os.system(command)
                os.chdir(curr_dir)
                break
            else:
                pullPath(filePath)


args = sys.argv
# 默认一个。 此脚本文件名
argsLen = len(args)
if 1 == argsLen:
    defPath = "/Users/nijianfeng/projects/"
    print(args[0] + " have no argrs!")
    str = input("do you want to pull " + defPath + " Y/N? << ")
    if (str == "Y" or str == "y"):
        pullPath(defPath)
    else:
        sys.exit(0)

for i in range(1, argsLen):
    path = args[i]
    if (os.path.isdir(path)):
        pullPath(path)
    else:
        print(path + " is not a dir!")
        continue
