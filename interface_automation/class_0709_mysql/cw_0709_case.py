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
import json
import re
import unittest

from ddt import ddt, data

from interface_automation.class_0709_mysql.cw_0709_config import do_config
from interface_automation.class_0709_mysql.cw_0709_excel import HandleExcel
from interface_automation.class_0709_mysql.cw_0709_log import do_logger
from interface_automation.class_0709_mysql.cw_0709_mysql import do_mysql
from interface_automation.class_0709_mysql.cw_0709_request import do_request

# file = config['file path']['case_path']
file = do_config.get_value('file path', 'case_path')
true_result = do_config.get_value('msg', 'true_result')
fail_result = do_config.get_value('msg', 'fail_result')


def excel_suite():
    not_existed_tel = do_mysql.not_existed_tel(do_config.get_value('mysql', 'not_existed_tel'))
    register_excel = HandleExcel(do_config.get_value('file path', 'case_path'), 'register')
    register_excel_cases = register_excel.get_case()
    register_excel_re = re.sub(r'\${not_existed_tel}', not_existed_tel, str(register_excel_cases))
    existed_tel = do_mysql.existed_tel(do_config.get_value('mysql', 'existed_tel'),
                                       do_config.get_int('mysql', 'existed_tel_type'))
    register_cases = re.sub(r'\${existed_tel}', existed_tel, str(register_excel_re))
    register_cases = eval(register_cases)
    wb, ws = register_excel.load_excel()
    wb.close()
    return register_cases


cases_suite = excel_suite()


def excel_suite1():
    not_existed_tel = do_mysql.not_existed_tel(do_config.get_value('mysql', 'not_existed_tel'))
    register_excel = HandleExcel(do_config.get_value('file path', 'case_path'), 'login')
    register_excel_cases = register_excel.get_case()
    register_excel_re = re.sub(r'\${not_existed_tel}', not_existed_tel, str(register_excel_cases))
    existed_tel = do_mysql.existed_tel(do_config.get_value('mysql', 'existed_tel'),
                                       do_config.get_int('mysql', 'existed_tel_type'))
    register_cases = re.sub(r'\${existed_tel}', existed_tel, str(register_excel_re))
    register_cases = eval(register_cases)
    wb, ws = register_excel.load_excel()
    wb.close()
    return register_cases


cases_suite1 = excel_suite1()


@ddt
class ApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('开始执行用例'))

    @classmethod
    def tearDownClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('用例执行结束'))

    def setUp(self):

        pass

    def tearDown(self):
        wb, ws = self.my_HandleExcel.load_excel()
        wb.save(file)
        wb.close()

    @data(*cases_suite)
    def test_register(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'register')
        request_result = do_request.send_request(case_list['method'],
                                                 do_config.get_value('request', 'default_address') + case_list[
                                                     'url_path'],
                                                 case_list['data'])
        actual_text = request_result.text
        actual_value = json.loads(actual_text)['code']
        actual = 'code: "{}",'.format(actual_value)
        result = case_list['expected']
        msg = case_list['title']
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e

    @data(*cases_suite1)
    def test_login(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'login')
        request_result = do_request.send_request(case_list['method'],
                                                 do_config.get_value('request', 'default_address') + case_list[
                                                     'url_path'],
                                                 case_list['data'])
        actual_text = request_result.text
        actual_value = json.loads(actual_text)['code']
        actual = 'code: "{}",'.format(actual_value)
        result = case_list['expected']
        msg = case_list['title']
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_list['case_id'] + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e


if __name__ == '__main__':
    unittest.main()
