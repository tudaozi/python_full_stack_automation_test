#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: task_2_2_str.py
@Time: 2019/5/22 16:42
@Desc: S
"""
"""
6.个人信息展示
在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
按照以下格式输出：
**************************************************
个人信息展示
​
姓名（网名）
​
年龄：年龄
性别：性别
爱好：爱好
座右铭：座右铭
**************************************************
"""
name = input("Please input your name：")
screen_name = input("Please input your screen_name：")
age = input("Please input your age：")
gender = input("Please input your gender：")
hobbies = input("Please input your hobbies：")
motto = input("Please input your motto：")

# 1
print('*' * 66 + '\n' + '个人信息展示')
print('\n' + name + '(' + screen_name + ')' + '\n')
print('年龄：' + age)
print('性别：' + gender)
print('爱好：' + hobbies)
print('座右铭：' + motto)
print('*' * 66)
# 2
print('*' * 66 + "\n个人信息展示\n\n%s(%s)\n\n年龄：%s\n性别：%s\n爱好：%s\n座右铭：%s\n" % (
    name, screen_name, age, gender, hobbies, motto) + '*' * 66)
# 3
print('*' * 66 + "\n个人信息展示\n\n{}({})\n\n年龄：{}\n性别：{}\n爱好：{}\n座右铭：{}\n".format(
    name, screen_name, age, gender, hobbies, motto) + '*' * 66)
