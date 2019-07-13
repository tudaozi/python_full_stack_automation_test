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

    @staticmethod
    def create_tel():
        tel_head = random.choice(['137', '138', '139'])
        tel_tail = ''.join(random.sample(string.digits, 8))
        full_tel = tel_head + tel_tail
        return full_tel

    def match_sql(self):
        if self.run(sql, args=(cr), ):
            return True
        else:
            return False

    def close(self):
        self.cursor.close()
        self.conn.close()


do_mysql = HandleMySQL()

if __name__ == '__main__':
    # sql = 'select * from member limit 0,10;'
    # sql = 'SELECT RegName,Pwd,MobilePhone FROM member WHERE MobilePhone =%s;'
    # sql = 'SELECT MobilePhone FROM member;'
    # one_mysql = do_mysql.run(sql, is_more=True)
    sql = 'SELECT MobilePhone FROM member WHERE %s;'
    print(type(do_mysql.create_tel(sql)))
    do_mysql.close()

    pass
