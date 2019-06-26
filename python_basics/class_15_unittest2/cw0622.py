#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw0622.py
@Time: 2019/6/26 9:03
@Desc: S
"""

# 将上节课的单元测试用例通过 suite 和 runner 执行
import unittest
from ..class_14_unittest1.cw0620 import TestExcel

suite = unittest.TestCase([TestExcel('test_None'), TestExcel('test_Equal')])
with open('..class_14_unittest1.cw0620.demo.xlsx', 'w', encoding='utf-8') as f:
    runner = unittest.TextTestRunner(f)
    runner.run(suite)
# 1、两种以上 suite 添加测试用例的方式。（loader)
# 2、使用 HTMLTestRunner 生成测试报告

if __name__ == 'main':
    unittest.main()
