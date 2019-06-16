#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: mora1.py
@Time: 2019-06-17 01:08
@Desc: S
"""


class Users:
    def __init__(self, user):
        self.user = user

    def add(self, serial, name):
        self.user[serial] = name

    # def __repr__(self):
    #     return self.user


class Mora:
    def __init__(self, optional_role):
        self.optional_role = optional_role

    def role_selection(self, serial_number):
        for t in self.optional_role.keys():
            if serial_number == t:
                return self.optional_role[t]

    @staticmethod
    def gap():
        print('\n\\\\', '*' * 69, '\n')


role = Users({})
print(role)
role.add(1, '曹操')
print(type(role.user))
role.add(2, '张飞')
print(role.user)
role.add(3, '刘备')
print(role.user)

my_mora = Mora(role.user)
print(my_mora.role_selection(2))
