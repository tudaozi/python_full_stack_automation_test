#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0625_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: S
"""
import unittest

from interface_automation.class_0629_log.test_cw0629_case import TestArithmetic

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestArithmetic))

if __name__ == '__main__':
    unittest.main()
