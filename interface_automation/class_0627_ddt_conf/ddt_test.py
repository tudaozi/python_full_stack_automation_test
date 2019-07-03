#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: ddt_test.py
@Time: 2019/7/3 11:59
@Desc: S
"""

import unittest
import ddt


@ddt.ddt
class Abc(unittest.TestCase):

    @ddt.data(['02', 's'], ['30', 'w'])
    # @ddt.unpack
    def testds001(self, m):
        print(m)

    # @ddt.file_data('../resource/test01.yaml')
    #     # @ddt.unpack
    #     # def testae003(self, m, n):
    #     #     print(m, n)

    @ddt.data([23, 3], [67, 3])
    #@ddt.unpack
    def testpd004(self, m):
        print(m)


if __name__ == '__main__':
    unittest.main()
