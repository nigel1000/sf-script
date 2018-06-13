#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/13

# 假设这个函数用来筛选用户
def filter(users, team_name):
    filter_users = {}
    start = min(users.keys())
    end = max(users.keys())
    for i in range(start, end):
        if users[i] == team_name:
            temp_user = {}
            temp_user[i] = users[i]
            filter_users.update(temp_user)
    return filter_users


# 假设这个函数发邮件
def send_email(user, email_content):
    start = min(user.keys())
    end = max(user.keys())
    flag = (start + end) / 2
    for i in range(start, end):
        if i < flag:
            user[i] += email_content[0]
        else:
            user[i] += email_content[1]
    return user


if __name__ == '__main__':
    # 用户字典
    users = {}
    # 初始化1万个用户
    for i in range(0, 10000):
        users[i] = ""

    # 第一轮发送邮件的内容
    email_content_1 = ["哥伦比亚", "乌拉圭"]
    # 发送邮件
    user = send_email(users, email_content_1)
    # 比赛结束，知道胜者为哥伦比亚，筛选用户
    users = filter(users, "哥伦比亚")

    # 第二轮邮件内容
    email_content_2 = ["比利时", "美国"]
    # 发送第二轮邮件
    users = send_email(users, email_content_2)
    # 比赛结束，知道胜者为比利时，筛选用户
    users = filter(users, "哥伦比亚比利时")

    start = min(users.keys())
    end = max(users.keys())
    for i in range(start, end):
        print(str(i+1) + ":" + users[i])
