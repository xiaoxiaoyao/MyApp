#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example.py 的全面测试用例

测试覆盖：
- MyClass 类的所有方法
- bad_function 函数
- 边界条件和异常场景

测试通过率目标：100%
"""

import unittest
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from example import MyClass, bad_function


class TestMyClass(unittest.TestCase):
    """MyClass 类的测试类"""

    def setUp(self):
        """测试前初始化"""
        self.obj = MyClass()

    def tearDown(self):
        """测试后清理"""
        pass

    def test_init_default_values(self):
        """测试初始化默认值"""
        self.assertEqual(self.obj.name, "")
        self.assertEqual(self.obj.age, 0)

    def test_set_name_normal(self):
        """测试正常设置姓名"""
        self.obj.set_name("张三")
        self.assertEqual(self.obj.name, "张三")

    def test_set_name_empty(self):
        """测试设置空姓名"""
        self.obj.set_name("")
        self.assertEqual(self.obj.name, "")

    def test_set_name_unicode(self):
        """测试设置中文姓名"""
        self.obj.set_name("李四")
        self.assertEqual(self.obj.name, "李四")

    def test_set_name_special_chars(self):
        """测试设置特殊字符姓名"""
        self.obj.set_name("Test@123")
        self.assertEqual(self.obj.name, "Test@123")

    def test_get_info_default(self):
        """测试默认情况下的 get_info"""
        info = self.obj.get_info()
        self.assertIn("Name: ", info)
        self.assertIn("Age: 0", info)

    def test_get_info_after_set(self):
        """测试设置后的 get_info"""
        self.obj.set_name("王五")
        self.obj.age = 25
        info = self.obj.get_info()
        self.assertIn("王五", info)
        self.assertIn("25", info)

    def test_age_modification(self):
        """测试年龄修改"""
        self.obj.age = 30
        self.assertEqual(self.obj.age, 30)

    def test_age_negative(self):
        """测试负数年龄"""
        self.obj.age = -5
        self.assertEqual(self.obj.age, -5)


class TestBadFunction(unittest.TestCase):
    """bad_function 函数的测试类"""

    def test_return_value(self):
        """测试返回值"""
        result = bad_function()
        self.assertEqual(result, 3)

    def test_return_type(self):
        """测试返回类型"""
        result = bad_function()
        self.assertIsInstance(result, int)

    def test_exception_handling(self):
        """测试异常处理（函数内部捕获了 ZeroDivisionError）"""
        # 函数内部捕获了异常，不会抛出
        try:
            result = bad_function()
            self.assertEqual(result, 3)
        except ZeroDivisionError:
            self.fail("bad_function() 不应该抛出 ZeroDivisionError")


class TestMyClassIntegration(unittest.TestCase):
    """MyClass 集成测试类"""

    def test_full_workflow(self):
        """测试完整工作流程"""
        obj = MyClass()
        
        # 初始状态
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.age, 0)
        
        # 设置姓名和年龄
        obj.set_name("测试用户")
        obj.age = 30
        
        # 验证状态
        self.assertEqual(obj.name, "测试用户")
        self.assertEqual(obj.age, 30)
        
        # 验证信息输出
        info = obj.get_info()
        self.assertIn("测试用户", info)
        self.assertIn("30", info)

    def test_multiple_instances(self):
        """测试多个实例独立"""
        obj1 = MyClass()
        obj2 = MyClass()
        
        obj1.set_name("实例1")
        obj2.set_name("实例2")
        obj1.age = 20
        obj2.age = 30
        
        self.assertEqual(obj1.name, "实例1")
        self.assertEqual(obj2.name, "实例2")
        self.assertEqual(obj1.age, 20)
        self.assertEqual(obj2.age, 30)


class TestEdgeCases(unittest.TestCase):
    """边界条件测试类"""

    def test_name_with_spaces(self):
        """测试带空格的姓名"""
        obj = MyClass()
        obj.set_name("张 三")
        self.assertEqual(obj.name, "张 三")

    def test_name_with_numbers(self):
        """测试带数字的姓名"""
        obj = MyClass()
        obj.set_name("User123")
        self.assertEqual(obj.name, "User123")

    def test_very_long_name(self):
        """测试超长姓名"""
        obj = MyClass()
        long_name = "A" * 1000
        obj.set_name(long_name)
        self.assertEqual(obj.name, long_name)

    def test_large_age(self):
        """测试超大年龄"""
        obj = MyClass()
        obj.age = 999999
        self.assertEqual(obj.age, 999999)


if __name__ == '__main__':
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestMyClass))
    suite.addTests(loader.loadTestsFromTestCase(TestBadFunction))
    suite.addTests(loader.loadTestsFromTestCase(TestMyClassIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))

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
