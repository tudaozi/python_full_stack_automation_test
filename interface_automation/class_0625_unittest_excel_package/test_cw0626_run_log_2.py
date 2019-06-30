#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0626_run_log_1.py
@Time: 2019-06-29 22:19
@Desc: S
"""
import unittest
from interface_automation.class_0625_unittest_excel_package import HTMLTestRunnerNew
from interface_automation.class_0625_unittest_excel_package.test_cw0626_case_suite_2 import suite

with open('test_resule_add_2.html', 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='四则运算测试用例报告',
                                              description='测试两数的四则运算',
                                              tester='刀刀')
    result.run(suite)
