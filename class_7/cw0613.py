#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw0613.py
@Time: 2019-06-18 23:51
@Desc: S
"""
import random


class Mora:
    def __init__(self, name):
        self.name = name
        print('{}猜拳游戏'.format(name))
        pass

    # 1）函数1：选择角色1 曹操 2张飞 3 刘备
    def select_role(self):
        role = {1: '曹操', 2: '张飞', 3: '刘备'}
        user_select = input('请选择角色，1曹操，2张飞，3刘备：')
        user_select = int(user_select)
        for r_key in role.keys():
            if user_select == r_key:
                return role[user_select]

    # 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
    def role_punch(self):
        user_punch = input('请出拳，1剪刀，2石头，3布：')
        user_punch = int(user_punch)
        return user_punch

    # 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
    def computer_punch(self):
        robot_punch = random.randint(1, 3)
        print(robot_punch)
        return robot_punch

    # 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
    def mora_punch(self):
        if (self.role_punch() < self.computer_punch() and self.computer_punch() - self.role_punch() == 1) \
                or (self.role_punch() > self.computer_punch() and self.computer_punch() - self.role_punch() == -2):
            print("你赢了")
            # self.score_name.append('赢')
        elif self.role_punch() == self.computer_punch():
            print("平局")
            # self.score_name.append('平')
        else:
            print("你输了")
            # self.score_name.append('输')

    # 41)判断用户是否继续猜拳
    def whether_mora(self):
        pass

    # 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束   [[用户,赢，平，输],[电脑，赢，平，输]]
    def output_result(self):

        pass


my_mora = Mora('树树')
my_mora.select_role()
my_mora.role_punch()
my_mora.role_punch()
my_mora.mora_punch()
