#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: creator.py
@time: 2023/9/16 14:31
@project: fluent-python
@desc: P62 从出版物记录中提取创作者的名字
"""


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            return ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            return ValueError(f'Invalid record: {record!r}')


if __name__ == '__main__':
    b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')
    print(get_creators(b1))
