#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ramanujan.py
@time: 2023/9/18 15:56
@project: fluent-python
@desc: P117 比较简单的str和bytes正则表达式的行为
"""
import re

# str类型
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
# bytes类型
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

# bytes正则表达式只能搜索bytes字符串
text_bytes = text_str.encode('utf_8')

print(f'Text\n  {text_str!r}')
print('Numbers')
# str模式r'\d+'只能匹配泰米尔数值和ASCII数字
print('  str  :', re_numbers_str.findall(text_str))
# bytes模式rb'\d+'只能匹配ASCII字节中的数字
print('  bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
# str模式r'\w+'能匹配字母、上标、泰米尔数字和ASCII数字
print('  str  :', re_words_str.findall(text_str))
# bytes模式rb'\w+'只能匹配ASCII字节中的字母和数字
print('  bytes:', re_words_bytes.findall(text_bytes))
