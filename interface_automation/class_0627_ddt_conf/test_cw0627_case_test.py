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


@ddt
class TestArithmetic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*HandleExcel(file, 'add').get_case())
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
            my_HandleExcel = HandleExcel(file, 'add')
            my_HandleExcel.write_result(case_id + 1, actual, 'Pass')
            wb, ws = my_HandleExcel.load_excel()
            wb.save(file)
            wb.close()
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            raise e

    @data(*HandleExcel(file, 'minus').get_case())
    def test_add(self, case_list):
        case_id = case_list['case_id']
        title = case_list['title']
        l_data = case_list['l_data']
        r_data = case_list['r_data']
        expected = case_list['expected']
        actual = Arithmetic(l_data, r_data).minus()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
            my_HandleExcel = HandleExcel(file, 'minus')
            my_HandleExcel.write_result(case_id + 1, actual, 'Pass')
            wb, ws = my_HandleExcel.load_excel()
            wb.save(file)
            wb.close()
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            raise e

    @data(*HandleExcel(file, 'multiply').get_case())
    def test_add(self, case_list):
        case_id = case_list['case_id']
        title = case_list['title']
        l_data = case_list['l_data']
        r_data = case_list['r_data']
        expected = case_list['expected']
        actual = Arithmetic(l_data, r_data).multiply()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
            my_HandleExcel = HandleExcel(file, 'multiply')
            my_HandleExcel.write_result(case_id + 1, actual, 'Pass')
            wb, ws = my_HandleExcel.load_excel()
            wb.save(file)
            wb.close()
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            raise e

    @data(*HandleExcel(file, 'division').get_case())
    def test_add(self, case_list):
        case_id = case_list['case_id']
        title = case_list['title']
        l_data = case_list['l_data']
        r_data = case_list['r_data']
        expected = case_list['expected']
        actual = Arithmetic(l_data, r_data).division()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
            my_HandleExcel = HandleExcel(file, 'division')
            my_HandleExcel.write_result(case_id + 1, actual, 'Pass')
            wb, ws = my_HandleExcel.load_excel()
            wb.save(file)
            wb.close()
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
