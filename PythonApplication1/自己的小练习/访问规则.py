#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 类变量访问规则示例
演示 Python 中类的私有变量、受保护变量和属性装饰器的使用
"""


class Person:
    """人类，演示类变量的访问规则。"""

    def __init__(self, name):
        """初始化 Person 实例。

        Args:
            name (str): 人的姓名
        """
        self.__name = name

    @property
    def age(self):
        """获取年龄。

        Returns:
            int: 人的年龄
        """
        return self._age

    @age.setter
    def age(self, value):
        """设置年龄。

        Args:
            value (int): 要设置的年龄

        Raises:
            ValueError: 当年龄不是整数或不在合理范围内时

        Note:
            必须使用 self._age 而不是 self.age，否则会导致递归调用栈溢出
        """
        if type(value) != int:
            raise ValueError('need a interger请输入一个数字')
        if not (0 < value < 150):
            raise ValueError('need a reasonable number请输入一个正常的年龄')
        self._age = value


def demo_access_rules():
    """演示 Python 类的访问规则。"""
    person = Person('小尧')
    person.age = 10

    print('hasattr(person, "age"):', hasattr(person, 'age'))
    print('hasattr(person, "_age"):', hasattr(person, '_age'))
    print('hasattr(person, "__name"):', hasattr(person, '__name'))

    print('\nPython对象权限机制并不阻止访问，一切皆靠自觉')
    try:
        print(person.__name)
        print(person.name)
    except AttributeError as e:
        print(e)
    finally:
        print(person._Person__name)
        print(person._age)
        print(person.age)


def main():
    """主函数，运行访问规则演示。"""
    demo_access_rules()


if __name__ == "__main__":
    main()
