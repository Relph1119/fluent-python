#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: default_encoding.py
@time: 2023/9/18 13:09
@project: fluent-python
@desc: P100 探索默认编码
"""

import locale
import sys

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(f'{expression:>30} -> {value!r}')

