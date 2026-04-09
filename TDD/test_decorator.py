#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decorator.py 的测试用例

测试覆盖：
- test_decorator 装饰器
- decorated_function 函数
- 边界条件和异常场景

测试通过率目标：100%
"""

import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from PythonApplication1.自己的小练习.decorator import test_decorator, decorated_function


class TestDecorator(unittest.TestCase):
    """装饰器测试类"""

    def test_decorator_basic(self):
        """测试装饰器基本功能"""
        # 定义一个测试函数
        @test_decorator
        def test_func():
            return "test"
        
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_func()
        output = f.getvalue()
        
        # 验证装饰器输出
        self.assertIn('装饰器开始', output)
        self.assertIn('装饰器结束', output)
        # 验证函数返回值
        self.assertEqual(result, "test")

    def test_decorator_with_arguments(self):
        """测试带参数的装饰器函数"""
        # 定义一个带参数的测试函数
        @test_decorator
        def test_func_with_args(a, b):
            return a + b
        
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_func_with_args(1, 2)
        output = f.getvalue()
        
        # 验证装饰器输出
        self.assertIn('装饰器开始', output)
        self.assertIn('装饰器结束', output)
        # 验证函数返回值
        self.assertEqual(result, 3)

    def test_decorator_with_keyword_arguments(self):
        """测试带关键字参数的装饰器函数"""
        # 定义一个带关键字参数的测试函数
        @test_decorator
        def test_func_with_kwargs(name, age):
            return f"{name}, {age}"
        
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_func_with_kwargs(name="张三", age=25)
        output = f.getvalue()
        
        # 验证装饰器输出
        self.assertIn('装饰器开始', output)
        self.assertIn('装饰器结束', output)
        # 验证函数返回值
        self.assertEqual(result, "张三, 25")


class TestDecoratedFunction(unittest.TestCase):
    """被装饰函数测试类"""

    def test_decorated_function_output(self):
        """测试被装饰函数的输出"""
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            decorated_function()
        output = f.getvalue()
        
        # 验证输出
        self.assertIn('装饰器开始', output)
        self.assertIn('被装饰函数执行', output)
        self.assertIn('装饰器结束', output)

    def test_decorated_function_return_value(self):
        """测试被装饰函数的返回值"""
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = decorated_function()
        
        # 验证返回值
        self.assertIsNone(result)


class TestDecoratorEdgeCases(unittest.TestCase):
    """装饰器边界条件测试类"""

    def test_decorator_with_no_arguments(self):
        """测试无参数的装饰器函数"""
        # 定义一个无参数的测试函数
        @test_decorator
        def test_func_no_args():
            pass
        
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            test_func_no_args()
        output = f.getvalue()
        
        # 验证装饰器输出
        self.assertIn('装饰器开始', output)
        self.assertIn('装饰器结束', output)

    def test_decorator_with_many_arguments(self):
        """测试带多个参数的装饰器函数"""
        # 定义一个带多个参数的测试函数
        @test_decorator
        def test_func_many_args(*args, **kwargs):
            return sum(args)
        
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_func_many_args(1, 2, 3, 4, 5)
        output = f.getvalue()
        
        # 验证装饰器输出
        self.assertIn('装饰器开始', output)
        self.assertIn('装饰器结束', output)
        # 验证函数返回值
        self.assertEqual(result, 15)


if __name__ == '__main__':
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestDecorator))
    suite.addTests(loader.loadTestsFromTestCase(TestDecoratedFunction))
    suite.addTests(loader.loadTestsFromTestCase(TestDecoratorEdgeCases))

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 输出测试统计
    print("\n" + "=" * 70)
    print("测试统计:")
    print(f"  运行测试数: {result.testsRun}")
    print(f"  通过测试数: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  失败测试数: {len(result.failures)}")
    print(f"  错误测试数: {len(result.errors)}")
    print(f"  通过率: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.2f}%")
    print("=" * 70)
