#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: python_full_stack_automation_test
@File: cw_0706_handle_request.py
@Time: 2019-07-08 01:01
@Desc: S
"""
import requests

# 1、构造请求的url
url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
# 2、创建请求参数
params = {
    'mobilephone': 13798288888,
    'pwd': 123456,
    'regname': '刀刀'
}
# 向服务器发起GET请求
res = requests.get(url, params=params)

pass
