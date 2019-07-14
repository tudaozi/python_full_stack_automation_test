#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test.py
@Time: 2019/7/13 1:22
@Desc: S
"""
# import pymysql
import random
import string

# from interface_automation.class_0709_mysql.cw_0709_config import do_config


def create_tel():
    tel_head = random.choice(['137', '138', '139'])
    tel_tail = ''.join(random.sample(string.digits, 8))
    full_tel = tel_head + tel_tail
    return full_tel


print(create_tel())
