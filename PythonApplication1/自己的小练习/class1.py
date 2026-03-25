﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的学生类示例
用于存储和显示学生信息
"""


class Student:
    """学生类，用于存储学生姓名和分数信息。"""

    def __init__(self, name: str, score: float):
        """初始化学生类实例。

        Args:
            name (str): 学生姓名
            score (float): 学生分数
        """
        self.name = name
        self.score = score

    def print_score(self):
        """打印学生的姓名和分数信息。"""
        print('%s: %s' % (self.name, self.score))



