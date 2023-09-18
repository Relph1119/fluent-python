#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: simplify.py
@time: 2023/9/18 14:14
@project: fluent-python
@desc: P109 去掉全部组合记号的函数
"""
import string

import unicodedata


def shave_marks(txt):
    """删除所有变音符"""
    # 把所有字符分解成基字符和组合记号
    norm_txt = unicodedata.normalize('NFD', txt)
    # 过滤所有组合记号
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    # 重组所有字符
    return unicodedata.normalize('NFC', shaved)


def shave_marks_latin(txt):
    """删除所有拉丁基字符上的变音符"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # 忽略拉丁基字符的变音符
        preserve.append(c)
        # 如果不是组合字符，那就是新的基字符
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)


single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': 'EUR',
    '…': '...',
    'Æ': 'AE',
    'æ': 'ae',
    'Œ': 'OE',
    'œ': 'oe',
    '™': '(TM)',
    '‰': '<per mille>',
    '†': '**',
    '‡': '***',
})

multi_map.update(single_map)  # <3>


def dewinize(txt):
    """把cp1252符号替换为ASCII字符或字符序列"""
    return txt.translate(multi_map)


def asciize(txt):
    # 去掉变音符
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    # 使用NFKC规范化形式把字符和码点组合起来
    return unicodedata.normalize('NFKC', no_marks)


if __name__ == '__main__':
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    print(shave_marks(order))
    greek = 'Ζέφυρος, Zéfiro'
    print(shave_marks(greek))

    print(dewinize(order))
    print(asciize(order))
