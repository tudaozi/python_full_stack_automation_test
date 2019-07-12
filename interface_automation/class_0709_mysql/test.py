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


tel_head = [137, 138, 139]
tel_tail_randoms = random.sample(string.digits, 8)
tel_tail = ''
for n in tel_tail_randoms:
    tel_tail += tel_tail.join(n)
full_tel = ''
for i in random.sample(tel_head, 1):
    full_tel += str(i) + tel_tail
print(full_tel)
pass
