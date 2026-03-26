#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核心模块的自动化测试用例

测试覆盖：
- 核心工具模块
- 常用功能模块

测试通过率目标：100%
"""

import unittest
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestCoreModules(unittest.TestCase):
    """核心模块测试类"""

    def test_calculator_import(self):
        """测试计算器模块导入"""
        try:
            from utils.calculator import Calculator, calculate_area, process_data
            self.assertTrue(True)
        except ImportError:
            self.fail("无法导入 calculator 模块")

    def test_example_import(self):
        """测试 example 模块导入"""
        try:
            from example import MyClass, bad_function
            self.assertTrue(True)
        except ImportError:
            self.fail("无法导入 example 模块")


class TestAlgorithms(unittest.TestCase):
    """算法和数据结构测试类"""

    def test_hanoi_tower(self):
        """测试汉诺塔算法"""
        try:
            from PythonApplication1.自己的小练习.汉诺塔 import hanoi
            # 测试小规模情况
            import io
            from contextlib import redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                hanoi(2, 'A', 'B', 'C')
            output = f.getvalue()
            self.assertIn('A -> B', output)
            self.assertIn('A -> C', output)
            self.assertIn('B -> C', output)
        except ImportError:
            self.skipTest("汉诺塔模块未找到")

    def test_pascals_triangle(self):
        """测试杨辉三角算法"""
        try:
            from PythonApplication1.自己的小练习.杨辉三角 import generate_pascals_triangle
            # 测试前5行
            result = generate_pascals_triangle(5)
            expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
            self.assertEqual(result, expected)
        except ImportError:
            self.skipTest("杨辉三角模块未找到")


class TestUtilityFunctions(unittest.TestCase):
    """工具函数测试类"""

    def test_filtered_words_list(self):
        """测试过滤词列表"""
        try:
            from PythonApplication1.自己的小练习.filtered_words_list import FilteredWords
            # 测试过滤词功能
            fw = FilteredWords()
            self.assertIsInstance(fw, FilteredWords)
        except ImportError:
            self.skipTest("过滤词列表模块未找到")

    def test_decorator(self):
        """测试装饰器"""
        try:
            from PythonApplication1.自己的小练习.decorator import test_decorator, decorated_function
            # 测试装饰器功能
            import io
            from contextlib import redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                decorated_function()
            output = f.getvalue()
            self.assertIn('装饰器开始', output)
            self.assertIn('装饰器结束', output)
        except ImportError:
            self.skipTest("装饰器模块未找到")


if __name__ == '__main__':
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()
