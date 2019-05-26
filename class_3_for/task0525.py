# 2.请写出if判断语句的格式
"""
答：
    if _____:
        _____

    elif _____:
        _____
    else:
        _____
"""

# # 3.求三个整数中的最大值   提示：三个整数使用input提示用户输入
# intA = input('输入一个整数A：')
# intA = int(intA)
# intB = input('输入一个整数B：')
# intB = int(intB)
# intC = input('输入一个整数C：')
# intC = int(intC)
#
# if intA > intB and intA > intC:
#     print(intA)
# elif intB > intA and intB > intC:
#     print(intB)
# elif intC > intA and intC > intB:
#     print(intC)
# else:
#     print('输入的整数相等')

# # 4.判断是否为闰年
# """
# 提示：
# 输入一个有效的年份（如：2019），判断是否为闰年
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
# """
#
# while True:
#     years = input('输入一个年份，如2019：')
#     years = int(years)
#     if years == 0:
#         break
#     elif years % 4 == 0 and years % 100 != 0:
#         print('%d是闰年' % (years,))
#     else:
#         print('{}不是闰年'.format(years))

# 5.分别使用for和while打印九九乘法表
"""
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
"""
for nums in range(8):
    for num in range(9):
        num *= 1
        print(num)
