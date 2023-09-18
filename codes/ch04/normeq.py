#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: normeq.py
@time: 2023/9/18 14:11
@project: fluent-python
@desc: P108 规范化Unicode字符串，准确比较
"""
from unicodedata import normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)
    print(nfc_equal(s1, s2))
    print(nfc_equal('A', 'a'))
