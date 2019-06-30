#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0626_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: S
"""
import unittest
from interface_automation.class_0625_unittest_excel_package.test_cw0626_case_1 import TestAdd

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

if __name__ == '__main__':
    unittest.main()
