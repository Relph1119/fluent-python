#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: index.py
@time: 2023/9/16 15:31
@project: fluent-python
@desc: P68 与index0.py相比，使用dict.setdefault
"""

import re

WORD_RE = re.compile(r'\w+')

index = {}
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
