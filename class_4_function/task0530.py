"""
1.函数有哪几种参数类型，分别有什么特点和作用？

2.函数的可变参数是什么？有哪几种？为什么要使用可变参数？
"""

"""
3.将两个变量的值进行交换（a = 100, b = 200）
交换之后，a = 200， b = 100
"""

# 2在函数内对全局变量重新赋值
a = 100
b = 200


def exchange():
    global a
    a = 200
    global b
    b = 100


exchange()
print(a, b)

# 3全局变量传入函数变为局部变量并重新赋值，然后返回局部变量的值给函数
a = 100
print(id(a))
b = 200
print(id(b))


def exchange(a, b):
    a = 200
    b = 100
    print(id(a))
    print(id(b))
    return a, b


a, b = exchange(a, b)
print(a, b)
print(id(a))
print(id(b))
print(exchange(a, b))

# 4. 将用户输入的所有数字相乘之后对20取余数,用户输入的数字个数不确定

# def remainder(*nums):
#     d_remainder = ''
#     d_nums = 1
#     for i in nums:
#         d_remainder = d_nums * i
#     r_remainders = d_remainder % 20
#     print(r_remainders)
#
#
# remainder(12, 21, 32)

"""
    
    5、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
    
    6、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
    
    7、通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
    
    8、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，
    然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
