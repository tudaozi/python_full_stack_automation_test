""""""
""""
1.编写如下程序
有两行数据，存放在txt文件里面：
url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
[{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
{'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！
"""

# def formattedData(file):
#     openFile = open(file, mode='r', encoding='utf-8')
#     documentContent = openFile.readlines()
#     listContent = []
#     for item in documentContent:
#         strSlice = item.strip('\n').split('@')
#         dictionaryContent = {}
#         for items in strSlice:
#             childSlice = items.split(':', 1)
#             dictionaryContent[childSlice[0]] = childSlice[1]
#         listContent.append(dictionaryContent)
#     print(listContent)
#     openFile.close()
#
#
# formattedData('urlFile.txt')
"""
2.编写如下程序
创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto
b.从第二行开始，每行添加具体信息，例如：
可优,17,男,臭美,Always Be Coding!
柠檬小姐姐,16,女,可优,Lemon is best!
c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
person_info = [{"name": "可优",
               "age": 17,
               "gender": "男",
               "hobby": "臭美",
               "motto": "Always Be Coding!"},
              {"name": "柠檬小姐姐",
               "age": 16,
               "gender": "女",
               "hobby": "可优",
               "motto": "Lemon is best!"},
              ]
d.将所有用户信息写入到txt文件中之后，然后再读出
e.有精力的同学可以试试，多种方法来读取文件，比如csv模块（不作要求）
注意：csv格式的数据，是以英文逗号分隔的
"""
# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
csvFile = open('csvFormat.txt', 'w+', encoding='utf-8')
# a.第一行添加如下内容：name,age,gender,hobby,motto
csvFile.writelines('name,age,gender,hobby,motto')
csvFile.seek(0, 0)
print(csvFile.read())
csvFile.close()
# b.从第二行开始，每行添加具体信息，例如：
# 可优,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!
csvFile = open('csvFormat.txt', 'a+', encoding='utf-8')
csvFile.writelines(['\n可优,17,男,臭美,Always Be Coding!\n', '柠檬小姐姐,16,女,可优,Lemon is best!'])
csvFile.seek(0, 0)
print(csvFile.read())
csvFile.close()

# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
"""person_info = [{"name": "可优", "age": 17,"gender": "男","hobby": "臭美","motto": "Always Be Coding!"},
{"name": "柠檬小姐姐","age": 16,"gender": "女","hobby": "可优","motto": "Lemon is best!"},]
"""
csvFile = open('csvFormat.txt', 'w+', encoding='utf-8')
person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
csvFile.writelines(str(person_info))
# d.将所有用户信息写入到txt文件中之后，然后再读出
csvFile.seek(0, 0)
print(csvFile.read())
csvFile.close()
