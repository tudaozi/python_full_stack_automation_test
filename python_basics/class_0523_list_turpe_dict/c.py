#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: c.py
@Time: 2019/5/22 1:39
@Desc: S
"""

person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
for i in person_info:
    dictContent = {}
    for j in i.items():
        # print(j[0]+str(j[1]))
        dictContent[j[0]] = j[1]
    print(dictContent)
