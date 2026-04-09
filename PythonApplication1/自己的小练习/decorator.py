#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器示例程序
演示 Python 中装饰器的使用方法

在面向对象（OOP）的设计模式中，decorator 被称为装饰模式。
OOP 的装饰模式需要通过继承和组合来实现，而 Python 除了能支持 OOP 的
decorator 外，直接从语法层次支持 decorator。Python 的 decorator
可以用函数实现，也可以用类实现。
"""

import time


def test_decorator(func):
    """测试装饰器，在函数调用前后打印日志。

    Args:
        func: 要装饰的函数

    Returns:
        function: 包装后的函数
    """
    def wrapper(*args, **kw):
        """包装函数，在函数调用前后打印日志。

        Args:
            *args: 位置参数
            **kw: 关键字参数

        Returns:
            原函数的返回值
        """
        print('装饰器开始')
        result = func(*args, **kw)
        print('装饰器结束')
        return result
    return wrapper


@test_decorator
def decorated_function():
    """被装饰的函数，用于测试装饰器功能。"""
    print('被装饰函数执行')


def log(func):
    """日志装饰器，在函数调用前后打印日志。

    Args:
        func: 要装饰的函数

    Returns:
        function: 包装后的函数
    """
    def wrapper(*args, **kw):
        """包装函数，在函数调用前后打印日志。

        Args:
            *args: 位置参数
            **kw: 关键字参数

        Returns:
            原函数的返回值
        """
        print('call 1 %s' % func.__name__)
        return func(*args, **kw)
    print('call 0 %s' % func.__name__)
    return wrapper


def main():
    """主函数，演示装饰器的使用。"""
    print(time.asctime())
    decorated_time = log(time.asctime)
    print(decorated_time())


if __name__ == "__main__":
    main()
    decorated_function()
