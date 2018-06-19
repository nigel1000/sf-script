#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/13

import sys
import os
import threading
import time

def_path = "/Users/nijianfeng/projects/"
paths = []
threads = []


class PullThread(threading.Thread):

    def __init__(self, path, delay):
        threading.Thread.__init__(self)
        self.__path = path
        self.__delay = delay

    def run(self):
        threadLock.acquire()
        print("开始 git pull：" + self.__path)
        # time.sleep(self.__delay)
        os.chdir(self.__path)
        os.system("git pull ")
        print("结束pull：" + self.__path)
        threadLock.release()


def pull_path(dir_path=def_path):
    files = os.listdir(dir_path)
    for f in files:
        file_path = dir_path + '/' + f
        if os.path.isdir(file_path):
            if f == ".git":
                paths.append(dir_path)
                break
            else:
                pull_path(file_path)


threadLock = threading.Lock()
args = sys.argv
# 默认一个。 此脚本文件名
argsLen = len(args)
if 1 == argsLen:
    print(args[0] + " have no args!")
    print("do you want to pull " + def_path)
    print("please input Y/N >>> ")
    if input() in ["Y", "y", "yes"]:
        pull_path()
    else:
        sys.exit(0)
else:
    for i in range(1, argsLen):
        if os.path.isdir(args[i]):
            pull_path(args[i])
        else:
            print(args[i] + " is not a dir!")
            continue
for i, p in enumerate(paths):
    t = PullThread(p, i)
    threads.append(t)
    t.start()
for temp in threads:
    temp.join()
