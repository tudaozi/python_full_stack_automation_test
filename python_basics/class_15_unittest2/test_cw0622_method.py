#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: test_cw0622_method.py
@Time: 2019-06-28 01:08
@Desc: S
"""

import unittest
from .cw0622 import MathMethod


class TestMathMethod(unittest.TestCase):
    def test_two_positive(self):
        MathMethod(1, 2).add()


if __name__ == '__main__':
    unittest.main()
