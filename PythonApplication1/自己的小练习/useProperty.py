#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 属性装饰器示例
演示 @property 装饰器的使用方法
"""


class MyClass:
    """简单类，用于测试。"""

    def __init__(self):
        self.name = ''

    def set_name(self, name):
        self.name = name


class Student:
    """学生类，使用传统的 getter/setter 方法。

    为了限制 score 的范围，通过 set_score() 方法来设置成绩，
    再通过 get_score() 来获取成绩，这样在 set_score() 方法里
    就可以检查参数。
    """

    def get_score(self):
        """获取学生成绩。

        Returns:
            int: 学生成绩
        """
        return self._score

    def set_score(self, value):
        """设置学生成绩。

        Args:
            value (int): 要设置的成绩

        Raises:
            ValueError: 当成绩不是整数或不在0-100范围内时
        """
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


def demo_student():
    """演示 Student 类的使用。"""
    student = Student()
    student.set_score(60)
    print('s.get_score()', student.get_score())

    try:
        student.set_score(9999)
    except ValueError as error:
        print(error)


class Student2:
    """学生类，使用 @property 装饰器。

    使用 Python 内置的 @property 装饰器把方法变成属性调用，
    这样既可以检查参数，又可以像属性一样访问。
    """

    @property
    def score(self):
        """获取学生成绩（属性访问方式）。

        Returns:
            int: 学生成绩
        """
        return self._score

    @score.setter
    def score(self, value):
        """设置学生成绩（属性赋值方式）。

        Args:
            value (int): 要设置的成绩

        Raises:
            ValueError: 当成绩不是整数或不在0-100范围内时
        """
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


def demo_student2():
    """演示 Student2 类的使用。"""
    student = Student2()
    student.score = 80
    print('s.score', student.score)

    try:
        student.score = 9999
    except ValueError as error:
        print(error)


def main():
    """主函数，运行两种属性访问方式的演示。"""
    print("--- 使用传统 getter/setter 方法 ---")
    demo_student()
    print("\n--- 使用 @property 装饰器 ---")
    demo_student2()


if __name__ == "__main__":
    main()
