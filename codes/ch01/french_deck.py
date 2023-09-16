#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: french_deck.py
@time: 2023/9/15 11:38
@project: fluent-python
@desc: P4 一摞Python风格的纸牌
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

