#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: index_default.py
@time: 2023/9/16 15:34
@project: fluent-python
@desc: 使用defaultdict代替setdefault方法
"""
import collections
import re

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list)
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
