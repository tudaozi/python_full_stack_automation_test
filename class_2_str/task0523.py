#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: task0523.py
@Time: 2019/5/24 0:34
@Desc: S
"""
# 1、删除如下列表中的"矮穷丑"，写出能想到的所有方法
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]

# 1
info.remove("矮穷丑")
print(info)

# 2
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
info.pop(3)
print(info)

# 3
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
del info[3]
print(info)

# 2、什么时候用列表、什么时候用元组、什么时候用字典？他们分别适合什么场景使用？
"""
答：1）需要增删改数据集的时候采用列表
    2）只希望使用固定的数据集，不需要更改数据的时候采用元组
    3）
    3）允许用户交互，提交修改删除数据的场景下使用，如：网站用户中心
    4）只允许用户查看数据的场景下使用，如：查看统计报表
"""

# 3、有5道小题：
"""

d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
e, 你进一步添加自己的兴趣，至少需要 3 项。一经确定，不可修改。
"""
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄

# 1
man_info = ['姓名', '性别', '年龄']
print(man_info)

# 2
man_info = ('姓名', '性别', '年龄')
print(man_info)

# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# 1
man_info1 = ['姓名', '性别', '年龄']
man_info1.append('身高')
man_info1.append('联系方式')
print(man_info1)
# 2
man_info2 = ['姓名', '性别', '年龄']
man_info3 = ['身高', '联系方式']
man_info2.extend(man_info3)
print(man_info2)

# c, 平台为了保护你的隐私，需要你删除你的练习方式；
