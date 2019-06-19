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
        self.store_results = [[], []]
        print('{}猜拳'.format(name))

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
        return robot_punch

    # 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
    def mora_punch(self):
        """

        :return: 分别是用户和电脑的输赢状态，1代表赢，2代表输，3代表平
        """
        role_punch = self.role_punch()
        computer_punch = self.computer_punch()
        if (role_punch < computer_punch and computer_punch - role_punch == 1) \
                or (role_punch > computer_punch and computer_punch - role_punch == -2):
            print("你赢了")
            self.store_results[0].append(1)
            self.store_results[1].append(2)
        elif role_punch == computer_punch:
            print("平局")
            self.store_results[0].append(3)
            self.store_results[1].append(3)
            return [3, 3]
        else:
            print("你输了")
            self.store_results[0].append(2)
            self.store_results[1].append(1)

    # 41)判断用户是否继续猜拳,最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
    def whether_mora(self):
        select_role = self.select_role()
        self.mora_punch()
        while True:
            status = input("是否继续猜拳？输入y继续，输入n退出")
            if status == 'y':
                self.mora_punch()
            elif status == 'n':
                with open('score.txt', 'a+', encoding='utf-8')as score:
                    role_winning = self.store_results[0].count(1)
                    role_draw = self.store_results[0].count(2)
                    role_defeat = self.store_results[0].count(3)
                    role_result = ['{}：{}赢，{}平，{}败'.format(select_role, role_winning, role_draw, role_defeat)]
                    computer_winning = self.store_results[1].count(1)
                    computer_draw = self.store_results[1].count(2)
                    computer_defeat = self.store_results[1].count(3)
                    computer_result = ['电脑：{}赢，{}平，{}败'.format(computer_winning, computer_draw, computer_defeat)]
                    score.writelines(str([role_result, computer_result]))
                    score.seek(0, 0)
                    print(score.read())
                break
            else:
                print('输入有误，请重新输入：')
                continue


my_mora = Mora('树树')
my_mora.whether_mora()
