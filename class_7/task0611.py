#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: task0611.py
@Time: 2019-06-13 22:43
@Desc: S
"""

"""
1、实现一个手机类，并实例化你的手机。
要求类里要有：属性+行为。 至少应该具有品牌，型号等信息。 拨打电话，发短信等功能。
尽量多的获取不同属性和使用不同的功能。
2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
3.列举3个生活中类和对象的例子，用代码表示。
4.编写如下程序
创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
5.编写如下程序
编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
二、选作题
1.编写如下程序
编写一个工具箱类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
"""
# 1、实现一个手机类，并实例化你的手机。
"""
共有属性：Color, screen, camera
实例属性：Brand, model, system type
实行行为：Call, text, take pictures
"""


class MobilePhone:
    screen = 'Touch'
    camera = 'Megapixel'

    def __init__(self, brand, color, model='Smartphone', system_type='Android', cellphone_number=13888888888):
        self.brand = brand
        self.color = color
        self.model = model
        self.system_type = system_type
        self.cellphone_number = cellphone_number

    def call(self):
        pass
