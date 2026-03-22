#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
加减乘除4个函数的单元测试，严格遵循PEP 8规范
https://docs.python.org/3/library/unittest.html
"""

import unittest


class ZeroMultiError(Exception):
    """
    自定义错误类型，当乘法运算中有乘数为0时抛出此异常。
    """
    pass


def add(a: float = 0, b: float = 0) -> float:
    """
    加法运算函数。

    Args:
        a (float): 第一个加数，默认值为0
        b (float): 第二个加数，默认值为0

    Returns:
        float: 两个数的和
    """
    return a + b


def minus(a: float, b: float) -> float:
    """
    减法运算函数。

    Args:
        a (float): 被减数
        b (float): 减数

    Returns:
        float: 两个数的差 (a - b)
    """
    return a - b


def multi(a: float, b: float) -> float:
    """
    乘法运算函数。

    Args:
        a (float): 第一个乘数
        b (float): 第二个乘数

    Returns:
        float: 两个数的乘积
    """
    return a * b


def multi_not_zero(a: float, b: float) -> float:
    """
    特殊乘法运算函数，要求乘数不能为0。

    Args:
        a (float): 第一个乘数
        b (float): 第二个乘数

    Raises:
        ZeroMultiError: 当任一乘数为0时抛出异常

    Returns:
        float: 两个数的乘积
    """
    if a == 0 or b == 0:
        raise ZeroMultiError('multi', [a, b])
    return a * b


def divide(a: float, b: float) -> float:
    """
    除法运算函数。

    Args:
        a (float): 被除数
        b (float): 除数

    Raises:
        ZeroDivisionError: 当除数为0时抛出异常

    Returns:
        float: 两个数的商 (a / b)
    """
    if b == 0:
        raise ZeroDivisionError('divide', b)
    return a / b


class TestMathFunc(unittest.TestCase):
    """
    测试 mathfunc.py 中的数学运算函数。
    """

    def setUp(self):
        """
        测试开始前的准备工作，每个测试用例都会执行此方法。
        """
        print('unittest start')
        self.a = 0
        self.b = 0

    def tearDown(self):
        """
        测试结束后的清理工作，每个测试用例都会执行此方法。
        """
        print('unittest ended')

    def test_add(self):
        """
        测试加法函数 add(a, b)。
        """
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """
        测试减法函数 minus(a, b)。
        """
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """
        测试乘法函数 multi(a, b)。
        """
        self.assertEqual(6, multi(2, 3))

    def test_multi_not_zero(self):
        """
        测试特殊乘法函数 multi_not_zero(a, b)。
        """
        self.assertEqual(6, multi_not_zero(2, 3))

    def test_divide(self):
        """
        测试除法函数 divide(a, b)。
        """
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def test_divide_error(self):
        """
        测试除法函数在除数为0时的异常处理。
        """
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_multi_not_zero_error(self):
        """
        测试特殊乘法函数在乘数为0时的异常处理。
        """
        with self.assertRaises(ZeroMultiError):
            multi_not_zero(5, 0)
            multi_not_zero(0, 0)
            multi_not_zero(0, 5)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        """
        测试跳过装饰器的使用，此测试永远不会运行。
        """
        self.fail("shouldn't happen")


if __name__ == '__main__':
    unittest.main()
