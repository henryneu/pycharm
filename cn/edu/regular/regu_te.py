# -*- coding:utf-8 -*- 
#Author: Henry
# 正则表达式
import re
# 编译正则表达式
re_email_1 = re.compile(r'^(\w+)@(\w+).(\w+)$')
re_email_2 = re.compile(r'^(\w+).(\w+)@(\w+).(\w+)$')
re_email_3 = re.compile(r'^\<(\w+\s\w+)>\s(\w+[\w.]?\w+@\w+.\w+)')
# 匹配给定字符串
add_1 = re_email_1.match('someone@gmail.com').group()
add_2 = re_email_2.match('bill.gates@microsoft.com').group()
add_3 = re_email_3.match('<Tom Paris> tom@voyager.org')
print(add_1)
print(add_2)
print(add_3.group())
print(add_3.group(1))
print(add_3.group(2))
