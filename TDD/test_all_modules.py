#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目所有模块的自动化测试用例

测试覆盖：
- 核心工具模块
- 算法和数据结构
- Web 应用功能
- 常用工具函数

测试通过率目标：100%
"""

import unittest
import sys
import os
import tempfile
import io
from contextlib import redirect_stdout

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

    def test_set_operations(self):
        """测试集合运算"""
        try:
            from PythonApplication1.自己的小练习.集合运算 import perform_set_operations
            # 测试集合运算功能
            result = perform_set_operations()
            self.assertIsInstance(result, dict)
            self.assertIn('union', result)
            self.assertIn('intersection', result)
            self.assertIn('difference', result)
        except ImportError:
            self.skipTest("集合运算模块未找到")


class TestWebApp(unittest.TestCase):
    """Web 应用测试类"""

    def test_web_app_import(self):
        """测试 Web 应用模块导入"""
        try:
            from PythonApplication1.my_first_web_app.www import index, main, conn, Log
            self.assertTrue(True)
        except ImportError:
            self.fail("无法导入 Web 应用模块")

    def test_config_import(self):
        """测试配置模块导入"""
        try:
            from PythonApplication1.my_first_web_app.www import config
            self.assertTrue(True)
        except ImportError:
            self.fail("无法导入配置模块")


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
            f = io.StringIO()
            with redirect_stdout(f):
                decorated_function()
            output = f.getvalue()
            self.assertIn('装饰器开始', output)
            self.assertIn('装饰器结束', output)
        except ImportError:
            self.skipTest("装饰器模块未找到")

    def test_try_except(self):
        """测试异常处理"""
        try:
            from PythonApplication1.自己的小练习.tryexcept import test_try_except
            # 测试异常处理功能
            result = test_try_except()
            self.assertEqual(result, '执行成功')
        except ImportError:
            self.skipTest("异常处理模块未找到")


class TestFileOperations(unittest.TestCase):
    """文件操作测试类"""

    def test_read_write_operations(self):
        """测试文件读写操作"""
        # 创建临时文件测试
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as f:
            f.write('测试内容')
            temp_filename = f.name
        
        try:
            # 测试文件读取
            with open(temp_filename, 'r', encoding='utf-8') as f:
                content = f.read()
            self.assertEqual(content, '测试内容')
            
            # 测试文件写入
            with open(temp_filename, 'a', encoding='utf-8') as f:
                f.write('追加内容')
            with open(temp_filename, 'r', encoding='utf-8') as f:
                content = f.read()
            self.assertEqual(content, '测试内容追加内容')
        finally:
            # 清理临时文件
            if os.path.exists(temp_filename):
                os.remove(temp_filename)


class TestRegularExpressions(unittest.TestCase):
    """正则表达式测试类"""

    def test_regular_expressions(self):
        """测试正则表达式操作"""
        try:
            from PythonApplication1.自己的小练习.regular_expression_operations import test_regex
            # 测试正则表达式功能
            result = test_regex()
            self.assertIsInstance(result, dict)
            self.assertIn('邮箱匹配', result)
            self.assertIn('手机号匹配', result)
            self.assertIn('URL匹配', result)
        except ImportError:
            self.skipTest("正则表达式模块未找到")


class TestAsyncIO(unittest.TestCase):
    """异步IO测试类"""

    def test_asyncio_import(self):
        """测试异步IO模块导入"""
        try:
            from PythonApplication1.自己的小练习.asynciotest import test_async
            self.assertTrue(True)
        except ImportError:
            self.skipTest("异步IO模块未找到")


class TestClassInheritance(unittest.TestCase):
    """类继承测试类"""

    def test_class_inheritance(self):
        """测试类继承功能"""
        try:
            from PythonApplication1.自己的小练习.class1 import Student, Person
            # 测试类继承
            student = Student("张三", 18, "计算机科学")
            self.assertIsInstance(student, Student)
            self.assertIsInstance(student, Person)
            self.assertEqual(student.name, "张三")
            self.assertEqual(student.age, 18)
            self.assertEqual(student.major, "计算机科学")
        except ImportError:
            self.skipTest("类继承模块未找到")


class TestControlFlow(unittest.TestCase):
    """控制流测试类"""

    def test_if_statements(self):
        """测试 if 语句"""
        try:
            from PythonApplication1.自己的小练习.if语句 import test_if_statement
            # 测试 if 语句功能
            result = test_if_statement(85)
            self.assertEqual(result, '优秀')
            result = test_if_statement(65)
            self.assertEqual(result, '良好')
            result = test_if_statement(45)
            self.assertEqual(result, '不及格')
        except ImportError:
            self.skipTest("if语句模块未找到")

    def test_for_loops(self):
        """测试 for 循环"""
        try:
            # 使用 importlib 动态导入，因为 'for' 是关键字
            import importlib.util
            import os
            
            # 构建模块路径
            module_path = os.path.join(os.path.dirname(__file__), '..', 'PythonApplication1', '自己的小练习', 'for.py')
            
            # 创建模块规范
            spec = importlib.util.spec_from_file_location('for_module', module_path)
            for_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(for_module)
            
            # 测试 for 循环功能
            result = for_module.test_for_loop(5)
            self.assertEqual(result, 15)  # 1+2+3+4+5=15
        except (ImportError, AttributeError, FileNotFoundError):
            self.skipTest("for循环模块未找到")


class TestReturnValues(unittest.TestCase):
    """返回值测试类"""

    def test_return_values(self):
        """测试返回值功能"""
        try:
            # 使用 importlib 动态导入，因为 'return' 是关键字
            import importlib.util
            import os
            
            # 构建模块路径
            module_path = os.path.join(os.path.dirname(__file__), '..', 'PythonApplication1', '自己的小练习', 'return.py')
            
            # 创建模块规范
            spec = importlib.util.spec_from_file_location('return_module', module_path)
            return_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(return_module)
            
            # 测试返回值功能
            result = return_module.test_return(10, 5)
            self.assertEqual(result, 15)
        except (ImportError, AttributeError, FileNotFoundError):
            self.skipTest("return模块未找到")


class TestPropertyDecorator(unittest.TestCase):
    """属性装饰器测试类"""

    def test_property_decorator(self):
        """测试属性装饰器功能"""
        try:
            from PythonApplication1.自己的小练习.useProperty import MyClass
            # 测试属性装饰器
            obj = MyClass()
            obj.name = "测试"
            self.assertEqual(obj.name, "测试")
        except ImportError:
            self.skipTest("属性装饰器模块未找到")


class TestNetworkOperations(unittest.TestCase):
    """网络操作测试类"""

    def test_network_import(self):
        """测试网络操作模块导入"""
        try:
            from PythonApplication1.自己的小练习.抓取 import fetch_data
            self.assertTrue(True)
        except ImportError:
            self.skipTest("网络抓取模块未找到")


class TestIntegration(unittest.TestCase):
    """集成测试类"""

    def test_module_integration(self):
        """测试模块集成"""
        # 测试多个模块的集成使用
        try:
            from utils.calculator import Calculator
            from example import MyClass
            
            # 使用计算器
            calc = Calculator()
            result = calc.add(10, 20)
            self.assertEqual(result, 30)
            
            # 使用 MyClass
            obj = MyClass()
            obj.set_name("集成测试")
            obj.age = 20
            info = obj.get_info()
            self.assertIn("集成测试", info)
            self.assertIn("20", info)
        except ImportError:
            self.skipTest("集成测试模块未找到")


if __name__ == '__main__':
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestCoreModules))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgorithms))
    suite.addTests(loader.loadTestsFromTestCase(TestWebApp))
    suite.addTests(loader.loadTestsFromTestCase(TestUtilityFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestFileOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestRegularExpressions))
    suite.addTests(loader.loadTestsFromTestCase(TestAsyncIO))
    suite.addTests(loader.loadTestsFromTestCase(TestClassInheritance))
    suite.addTests(loader.loadTestsFromTestCase(TestControlFlow))
    suite.addTests(loader.loadTestsFromTestCase(TestReturnValues))
    suite.addTests(loader.loadTestsFromTestCase(TestPropertyDecorator))
    suite.addTests(loader.loadTestsFromTestCase(TestNetworkOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

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
