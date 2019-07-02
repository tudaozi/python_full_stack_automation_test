#!/usr/bin/env python
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

from ddt import ddt, data

from interface_automation.class_0627_ddt_conf.cw0627_testing_object import Arithmetic
from interface_automation.class_0627_ddt_conf.test_cw0627_excel_package import HandleExcel

file = 'demo.xlsx'
my_excel = HandleExcel(file)
case_list = my_excel.get_case()


@ddt
class TestArithmetic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        pass

    @classmethod
    def tearDownClass(cls):
        wb, ws = my_excel.load_excel()
        wb.save(file)
        wb.close()

    @data(*case_list)
    def test_add(self, case_list):
        case_id = case_list['case_id']
        title = case_list['title']
        l_data = case_list['l_data']
        r_data = case_list['r_data']
        expected = case_list['expected']
        actual = Arithmetic(l_data, r_data).add()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
            my_excel.write_result(case_id + 1, actual, 'Pass')
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            raise e

    # def test_minus(self):
    #     self.ws_2 = self.file_2['minus']
    #     my_excel = HandleExcel(self.file_name_2, 'minus')
    #     for index, case_list in enumerate(my_excel.get_case()):
    #         real_result = Arithmetic(case_list['l_data'], case_list['r_data']).minus()
    #         expect_result = case_list['expected']
    #         msg = case_list['title']
    #         try:
    #             self.assertEqual(expect_result, real_result, msg)
    #             print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.file_1.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Pass'
    #         except AssertionError as e:
    #             print('具体异常为{}'.format(e))
    #             self.file_1.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Fail'
    #             raise e
    #
    # def test_multiply(self):
    #     self.ws_2 = self.file_2['multiply']
    #     my_excel = HandleExcel(self.file_name_2, 'multiply')
    #     for index, case_list in enumerate(my_excel.get_case()):
    #         real_result = Arithmetic(case_list['l_data'], case_list['r_data']).multiply()
    #         expect_result = case_list['expected']
    #         msg = case_list['title']
    #         try:
    #             self.assertEqual(expect_result, real_result, msg)
    #             print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.file_1.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Pass'
    #         except AssertionError as e:
    #             print('具体异常为{}'.format(e))
    #             self.file_1.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Fail'
    #             raise e
    #
    # def test_division(self):
    #     self.ws_2 = self.file_2['division']
    #     my_excel = HandleExcel(self.file_name_2, 'division')
    #     for index, case_list in enumerate(my_excel.get_case()):
    #         real_result = Arithmetic(case_list['l_data'], case_list['r_data']).division()
    #         expect_result = case_list['expected']
    #         msg = case_list['title']
    #         try:
    #             self.assertEqual(expect_result, real_result, msg)
    #             print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.file_1.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Pass'
    #         except AssertionError as e:
    #             print('具体异常为{}'.format(e))
    #             self.file_1.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
    #             self.ws_2.cell(index + 2, 6).value = real_result
    #             self.ws_2.cell(index + 2, 7).value = 'Fail'
    #             raise e


if __name__ == '__main__':
    unittest.main()
