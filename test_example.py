#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example.py 的测试用例
"""

import unittest
from example import MyClass, bad_function


class TestExample(unittest.TestCase):
    """测试example.py中的类和函数"""

    def test_myclass_init(self):
        """测试MyClass初始化"""
        obj = MyClass()
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.age, 0)

    def test_myclass_set_name(self):
        """测试set_name方法"""
        obj = MyClass()
        obj.set_name("张三")
        self.assertEqual(obj.name, "张三")

    def test_myclass_get_info(self):
        """测试get_info方法"""
        obj = MyClass()
        obj.set_name("李四")
        obj.age = 25
        info = obj.get_info()
        self.assertIn("李四", info)
        self.assertIn("25", info)

    def test_bad_function(self):
        """测试bad_function函数"""
        result = bad_function()
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
