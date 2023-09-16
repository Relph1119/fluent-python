#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: vector2d.py
@time: 2023/9/15 11:39
@project: fluent-python
@desc: P9 一个简单的二维向量类
"""
import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)