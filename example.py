#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例Python文件 - 修复版
严格遵循PEP8规范
"""

import os
import sys
from datetime import datetime


class MyClass:
    """示例类，用于存储姓名和年龄信息。"""

    def __init__(self):
        """初始化MyClass实例，设置默认姓名为空字符串，年龄为0。"""
        self.name = ""
        self.age = 0

    def get_info(self):
        """获取对象的姓名和年龄信息。

        Returns:
            str: 格式化的姓名和年龄字符串
        """
        return f"Name: {self.name}, Age: {self.age}"

    def set_name(self, name):
        """设置对象的姓名。

        Args:
            name (str): 要设置的姓名
        """
        self.name = name


def bad_function():
    """示例函数，演示加法运算和异常处理。

    Returns:
        int: x + y 的结果
    """
    x = 1
    y = 2
    z = x + y
    print(z)
    try:
        # 注意：此除零操作为示例代码，仅用于演示异常处理
        # 在实际生产代码中应避免此类故意的错误操作
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"捕获到除零异常: {e}")
    return z


if __name__ == "__main__":
    obj = MyClass()
    obj.set_name("test")
    print(obj.get_info())
    bad_function()
