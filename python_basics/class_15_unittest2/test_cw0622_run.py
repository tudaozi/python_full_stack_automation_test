#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0622_run.py
@Time: 2019-06-28 01:22
@Desc: S
"""
import unittest
from ..class_15_unittest2 import test_cw0622_suite

runner = unittest.TextTestRunner()
runner.run(test_cw0622_suite.suite)
