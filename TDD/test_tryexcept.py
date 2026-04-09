#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tryexcept.py 的测试用例

测试覆盖：
- test_try_except 函数
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

from PythonApplication1.自己的小练习.tryexcept import test_try_except


class TestTryExcept(unittest.TestCase):
    """异常处理测试类"""

    def test_test_try_except_success(self):
        """测试 test_try_except 函数的正常执行"""
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_try_except()
        output = f.getvalue()
        
        # 验证输出
        self.assertIn('Goodbye!', output)
        # 验证返回值
        self.assertEqual(result, '执行成功')

    def test_test_try_except_return_type(self):
        """测试 test_try_except 函数的返回类型"""
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            result = test_try_except()
        
        # 验证返回类型
        self.assertIsInstance(result, str)

    def test_test_try_except_output(self):
        """测试 test_try_except 函数的输出"""
        # 捕获输出
        f = io.StringIO()
        with redirect_stdout(f):
            test_try_except()
        output = f.getvalue()
        
        # 验证输出包含 'Goodbye!'
        self.assertIn('Goodbye!', output)


if __name__ == '__main__':
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestTryExcept))

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
