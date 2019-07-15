# !/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0625_case_1.py
@Time: 2019-06-29 22:18
@Desc: S
"""
import unittest
import re
from ddt import ddt, data

from interface_automation.class_0709_mysql.cw_0709_config import do_config
from interface_automation.class_0709_mysql.cw_0709_log import do_logger
from interface_automation.class_0709_mysql.cw_0709_mysql import do_mysql
from interface_automation.class_0709_mysql.cw_0709_excel import HandleExcel

# file = config['file path']['case_path']
file = do_config.get_value('file path', 'case_path')
true_result = do_config.get_value('msg', 'true_result')
fail_result = do_config.get_value('msg', 'fail_result')


@ddt
class ApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('开始执行用例'))
        not_existed_tel=do_mysql.not_existed_tel(do_config.get_int('mysql','not_existed_tel'))
        register=HandleExcel(file, 'register').get_case()
        pass

    @classmethod
    def tearDownClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('用例执行结束'))

    def setUp(self):
        pass

    def tearDown(self):
        wb, ws = self.my_HandleExcel.load_excel()
        wb.save(file)
        wb.close()

    @data(*HandleExcel(file, 'add').get_case())
    def test_add(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'add')
        case_id, title, l_data, r_data, expected = case_list['case_id'], case_list['title'], case_list['l_data'], \
                                                   case_list['r_data'], case_list['expected']
        actual = ApiTest(l_data, r_data).add()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_id + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_id + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e


if __name__ == '__main__':
    unittest.main()
