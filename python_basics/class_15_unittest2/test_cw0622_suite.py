#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0622_suite.py
@Time: 2019-06-28 01:10
@Desc: S
"""
# # 将上节课的单元测试用例通过 suite 和 runner 执行
# import unittest
# from .cw0620test import TestExcel
#
# suite = unittest.TestSuite()
# suite.addTest(TestExcel('test_none'))
# runner = unittest.TextTestRunner()
# runner.run(suite)
# # 1、两种以上 suite 添加测试用例的方式。（loader)
# # 2、使用 HTMLTestRunner 生成测试报告
#
# if __name__ == '__main__':
#     unittest.main()


import unittest
from .test_cw0622_method import TestMathMethod

suite = unittest.TestSuite()
suite.addTest(TestMathMethod('test_two_positive'))

if __name__ == '__main__':
    unittest.main()
