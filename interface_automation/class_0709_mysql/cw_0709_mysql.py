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

    def close(self):
        self.conn.close()


do_mysql = HandleMySQL()

if __name__ == '__main__':
    sql = 'select * from member limit 0,10;'
    one_mysql = do_mysql.run(sql, is_more=True)
    print(one_mysql)
    do_mysql.close()
    pass
