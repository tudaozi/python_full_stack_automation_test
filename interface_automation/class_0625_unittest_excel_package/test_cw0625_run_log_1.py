#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0625_run_log_1.py
@Time: 2019-06-29 22:19
@Desc: S
"""
from interface_automation.class_0625_unittest_excel_package import HTMLTestRunnerNew
from interface_automation.class_0625_unittest_excel_package.test_cw0625_case_suite_1 import suite

with open('test_resule_add_1.html', 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='加法测试用例', description='测试两数相加',
                                              tester='刀刀')
    result.run(suite)
