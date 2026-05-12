#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的学生类示例
用于存储和显示学生信息
"""


class Person:
    """人类，用于存储基本信息。"""

    def __init__(self, name: str, age: int):
        """初始化人类实例。

        Args:
            name (str): 姓名
            age (int): 年龄
        """
        self.name = name
        self.age = age


class Student(Person):
    """学生类，继承自Person，用于存储学生姓名、年龄和专业信息。"""

    def __init__(self, name: str, age: int, major: str):
        """初始化学生类实例。

        Args:
            name (str): 学生姓名
            age (int): 学生年龄
            major (str): 学生专业
        """
        super().__init__(name, age)
        self.major = major



