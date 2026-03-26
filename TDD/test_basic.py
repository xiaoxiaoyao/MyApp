#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础模块的自动化测试用例

测试覆盖：
- 核心工具模块
- 基础功能模块

测试通过率目标：100%
"""

import unittest
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestBasicModules(unittest.TestCase):
    """基础模块测试类"""

    def test_calculator(self):
        """测试计算器模块"""
        try:
            from utils.calculator import Calculator
            calc = Calculator()
            result = calc.add(2, 3)
            self.assertEqual(result, 5)
        except ImportError:
            self.skipTest("计算器模块未找到")

    def test_example(self):
        """测试 example 模块"""
        try:
            from example import MyClass
            obj = MyClass()
            obj.set_name("测试")
            self.assertEqual(obj.name, "测试")
        except ImportError:
            self.skipTest("example 模块未找到")

    def test_file_exists(self):
        """测试文件存在性"""
        # 测试核心文件是否存在
        files_to_check = [
            'utils/calculator.py',
            'example.py',
            'TDD/test_calculator.py',
            'TDD/test_example.py'
        ]
        
        for file_path in files_to_check:
            full_path = os.path.join(os.path.dirname(__file__), '..', file_path)
            self.assertTrue(os.path.exists(full_path), f"文件不存在: {file_path}")


if __name__ == '__main__':
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()
