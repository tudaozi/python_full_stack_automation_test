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
        print('品牌：{}，颜色：{}，类型：{}，系统：{}，号码：{}'.format(brand, color, model,
                                                     system_type,
                                                     cellphone_number))

    def call(self, caller, answer):
        print('{}使用{}号码打电话给{}'.format(caller, self.cellphone_number, answer))

    @staticmethod
    def gap():
        print('\n\\\\', '*' * 69, '\n')


daodao_phone = MobilePhone('Daodao', 'black')
print('类属性1：', MobilePhone.screen)
print('类属性2：', MobilePhone.camera)
daodao_phone.call('Daodao', 'Friend')
daodao_phone.gap()
friend_phone = MobilePhone('Friend', 'yellow', system_type='IOS', cellphone_number=13999999999)
friend_phone.call('Friend', 'Daodao')
daodao_phone.gap()

# 2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
"""
a.根据以上信息，抽象出一个类
b.定义相关属性，并能在类的外面调用
c.定义相关方法，在方法中打印相应信息
"""


class Cat:
    head = '一个猫头'
    foot = '四只脚'
    tail = '一条尾巴'
    skin = '皮肤多毛'
    print('这是一个有{},{}，{}，{}的一只猫'.format(head, foot, tail, skin))

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
        print('{}的{}猫，今年{}岁'.format(color, name, age))

    def eating(self, food):
        return '{}的{}猫，今年{}岁,吃着美味的{}'.format(self.color, self.name, self.age, food)

    def enjoy(self):
        print(self.eating(self.foot), '非常享受的样子')


daodao_cat = Cat
print('类属性1：', daodao_cat.head)
print('类属性2：', daodao_cat.foot)
print('类属性3：', daodao_cat.tail)
print('类属性4：', daodao_cat.skin)
daodao_phone.gap()
duoduo_cat = Cat('黄色', 'Tom', 2)
print(duoduo_cat.eating('猫粮'))
duoduo_cat.enjoy()

# 3.列举3个生活中类和对象的例子，用代码表示。
