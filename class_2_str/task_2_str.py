#!/usr/bin/env python
# coding=UTF-8
"""
@Author: 刀刀
@Contact: 1626202029
@Project: python_full_stack_automation_test
@File: task_2_str.py
@Time: 2019/5/22 0:42
@Desc: 字符串相关课程
"""
"""
    1、定义字符串I'm Lemon, I love Python automated testing！
    提示：使用双引号还是单引号呢？
"""
print("\n1、定义字符串I'm Lemon, I love Python automated testing！")
a = "I'm Lemon, I love Python automated testing！"
print(a + '\n' + '=' * 66)
"""
    2.把website = 'http://www.python.org'中的python字符串取出来
    提示：可以使用字符串切片
"""
print("\n2.把website = 'http://www.python.org'中的python字符串取出来")
# 1
print('\n#1')
b = "website = 'http://www.python.org'"
print(b[22:28])
# 2
print('\n#2')
website = 'http://www.python.org'
print(website[11:17] + '\n' + '=' * 66)
"""
    3.将给定字符串前后的空格除去，把PHP替换为Python
    best_language = "     PHP is the best programming language in the world!      "。左右各有一个空格。
"""
print("\n3.将给定字符串前后的空格除去，把PHP替换为Python")
# 1
print('\n#1')
c = 'best_language = " PHP is the best programming language in the world! "'
d = c[0:17]
e = c[17:-1]
f = e.strip().replace('PHP', 'Python')
g = f.lstrip()
h = c[-1]
print(d + g + h)
# 2
print('\n#2')
best_language = " PHP is the best programming language in the world! "
print(best_language.strip().lstrip().replace('PHP', 'Python') + '\n' + '=' * 66)
