#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calculator.py 的全面测试用例

测试覆盖：
- 正常功能测试
- 边界条件测试
- 异常场景测试
- 性能测试（大数运算）

测试通过率目标：100%
"""

import unittest
import sys
import os
import math

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.calculator import Calculator, calculate_area, process_data


class TestCalculatorBasic(unittest.TestCase):
    """计算器基础功能测试类"""

    def setUp(self):
        """测试前初始化"""
        self.calc = Calculator()

    def tearDown(self):
        """测试后清理"""
        pass

    # ==================== 加法测试 ====================
    def test_add_positive_numbers(self):
        """测试正数加法"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """测试负数加法"""
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_add_zero(self):
        """测试加零"""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        """测试浮点数加法"""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0, places=7)

    # ==================== 减法测试 ====================
    def test_subtract_positive_numbers(self):
        """测试正数减法"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        """测试负数减法"""
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_zero(self):
        """测试减零"""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ==================== 乘法测试 ====================
    def test_multiply_positive_numbers(self):
        """测试正数乘法"""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiply_negative_numbers(self):
        """测试负数乘法"""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_zero(self):
        """测试乘零"""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    # ==================== 除法测试 ====================
    def test_divide_positive_numbers(self):
        """测试正数除法"""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        """测试负数除法"""
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertIn("除数不能为零", str(context.exception))

    def test_divide_float_result(self):
        """测试浮点数除法结果"""
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    # ==================== 幂运算测试 ====================
    def test_power_positive(self):
        """测试正指数幂"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(3, 2), 9)

    def test_power_zero(self):
        """测试零指数"""
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(100, 0), 1)

    def test_power_negative(self):
        """测试负指数"""
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(4, -2), 0.0625)


class TestCalculatorEdgeCases(unittest.TestCase):
    """计算器边界条件测试类"""

    def setUp(self):
        self.calc = Calculator()

    def test_large_numbers(self):
        """测试大数运算"""
        result = self.calc.add(10**10, 10**10)
        self.assertEqual(result, 2 * 10**10)

    def test_small_numbers(self):
        """测试小数运算"""
        result = self.calc.add(1e-10, 1e-10)
        self.assertAlmostEqual(result, 2e-10, places=20)

    def test_very_large_power(self):
        """测试大数幂运算"""
        result = self.calc.power(2, 100)
        self.assertEqual(result, 1267650600228229401496703205376)

    def test_float_precision(self):
        """测试浮点数精度"""
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)


class TestCalculateArea(unittest.TestCase):
    """圆面积计算函数测试类"""

    def test_area_positive_radius(self):
        """测试正半径"""
        result = calculate_area(1)
        self.assertAlmostEqual(result, math.pi, places=7)

    def test_area_zero_radius(self):
        """测试零半径"""
        result = calculate_area(0)
        self.assertEqual(result, 0)

    def test_area_float_radius(self):
        """测试浮点半径"""
        result = calculate_area(2.5)
        expected = math.pi * 2.5 * 2.5
        self.assertAlmostEqual(result, expected, places=7)

    def test_area_large_radius(self):
        """测试大半径"""
        result = calculate_area(1000)
        expected = math.pi * 1000 * 1000
        self.assertAlmostEqual(result, expected, places=2)


class TestProcessData(unittest.TestCase):
    """数据处理函数测试类"""

    def test_process_positive_numbers(self):
        """测试正数处理"""
        data = [1, 2, 3, 4, 5]
        result = process_data(data)
        self.assertEqual(result, [2, 4, 6, 8, 10])

    def test_process_negative_numbers(self):
        """测试负数处理"""
        data = [-1, -2, -3]
        result = process_data(data)
        self.assertEqual(result, [0, 0, 0])

    def test_process_zero(self):
        """测试零处理"""
        data = [0, 0, 0]
        result = process_data(data)
        self.assertEqual(result, [0, 0, 0])

    def test_process_mixed(self):
        """测试混合数据"""
        data = [1, -2, 3, 0, 5]
        result = process_data(data)
        self.assertEqual(result, [2, 0, 6, 0, 10])

    def test_process_empty_list(self):
        """测试空列表"""
        data = []
        result = process_data(data)
        self.assertEqual(result, [])

    def test_process_floats(self):
        """测试浮点数"""
        data = [1.5, -2.5, 3.0]
        result = process_data(data)
        self.assertEqual(result, [3.0, 0, 6.0])


class TestCalculatorIntegration(unittest.TestCase):
    """计算器集成测试类"""

    def setUp(self):
        self.calc = Calculator()

    def test_chain_operations(self):
        """测试链式运算"""
        # (1 + 2) * 3 - 4 = 5
        result = self.calc.add(1, 2)
        result = self.calc.multiply(result, 3)
        result = self.calc.subtract(result, 4)
        self.assertEqual(result, 5)

    def test_complex_calculation(self):
        """测试复杂计算"""
        # ((10 - 3) * 2 + 8) / 3 = 8
        step1 = self.calc.subtract(10, 3)  # 7
        step2 = self.calc.multiply(step1, 2)  # 14
        step3 = self.calc.add(step2, 8)  # 22
        result = self.calc.divide(step3, 3)  # 7.333...
        self.assertAlmostEqual(result, 7.333333, places=5)


if __name__ == '__main__':
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorBasic))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculateArea))
    suite.addTests(loader.loadTestsFromTestCase(TestProcessData))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorIntegration))

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
