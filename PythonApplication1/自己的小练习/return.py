﻿﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
闭包函数示例程序
演示 Python 中闭包（Closure）的使用方式
"""


def count():
    """创建一个返回函数列表的函数。

    该函数演示了闭包的使用，每个返回的函数
    都捕获了当前循环变量 i 的值。

    Returns:
        list: 包含三个函数的列表
    """
    def f(j):
        """内部函数，创建一个返回 j*j 的函数。

        Args:
            j (int): 要计算平方的数字

        Returns:
            function: 返回 j*j 的函数
        """
        def g():
            """计算 j 的平方。

            Returns:
                int: j 的平方
            """
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


if __name__ == "__main__":
    functions = count()
    for func in functions:
        print(func())
