#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: index0.py
@time: 2023/9/16 15:28
@project: fluent-python
@desc: P67 使用dict.get获取并更新词出现的位置列表，编制索引
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
            # 这样写不完美
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

for word in sorted(index, key=str.upper):
    print(word, index[word])
