#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw_0709_mysql.py
@Time: 2019-07-11 00:26
@Desc: S
"""

import random
import string

import pymysql

from interface_automation.class_0709_mysql.cw_0709_config import do_config


class HandleMySQL:
    def __init__(self):
        self.conn = pymysql.connect(
            host=do_config.get_value('mysql', 'host'),
            user=do_config.get_value('mysql', 'user'),
            password=do_config.get_value('mysql', 'password'),
            db=do_config.get_value('mysql', 'db'),
            port=do_config.get_int('mysql', 'port'),
            charset=do_config.get_value('mysql', 'charset'),
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    # 随机创建一个手机号码
    def create_tel(self):
        tel_head = random.choice(['137', '138', '139'])
        tel_tail = ''.join(random.sample(string.digits, 8))
        full_tel = tel_head + tel_tail
        return full_tel

    # 返回一个数据库中的
    def existed_tel(self, sql, type=None):
        existed_tel = self.run(sql=sql, args=(type), )
        if existed_tel:
            return existed_tel['MobilePhone']
        else:
            print('数据库中没有该类型的手机号码')

    # 创建一个数据库中没有的手机号码
    def not_existed_tel(self, sql):
        while True:
            full_tel = self.create_tel()
            if not self.run(sql=sql, args=(full_tel), ):
                return full_tel

    def close(self):
        self.cursor.close()
        self.conn.close()


do_mysql = HandleMySQL()

if __name__ == '__main__':
    user_type = 1
    not_existed_tel = do_mysql.not_existed_tel('SELECT MobilePhone FROM member WHERE MobilePhone=%s;')
    print('数据库中不存在的手机号码为：{}'.format(not_existed_tel))
    existed_tel = do_mysql.existed_tel('SELECT MobilePhone FROM member WHERE Type=%s LIMIT 0,1;', user_type)
    print('数据库中已存在的手机号码为：{}'.format(existed_tel))
    do_mysql.close()

pass
