#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合运算示例程序
演示 Python 中两个列表的交、并、差（补）、对称差集的计算方法
"""


def demonstrate_set_operators(a, b):
    """使用集合运算符演示集合运算。

    Args:
        a (list): 第一个列表
        b (list): 第二个列表
    """
    print("1.1 使用集合运算符：")
    print(f"原始列表 a: {a}")
    print(f"原始列表 b: {b}")
    print(f"交集: {list(set(a) & set(b))}")
    print(f"并集: {list(set(a) | set(b))}")
    print(f"差集 (b - a): {list(set(b) - set(a))}")
    print(f"差集 (a - b): {list(set(a) - set(b))}")
    print(f"对称差集: {list(set(a) ^ set(b))}")


def demonstrate_set_methods(a, b):
    """使用集合方法演示集合运算（推荐方式）。

    Args:
        a (list): 第一个列表
        b (list): 第二个列表
    """
    print("\n1.2 使用集合方法：")
    print(f"原始列表 a: {a}")
    print(f"原始列表 b: {b}")
    print(f"交集: {list(set(a).intersection(set(b)))}")
    print(f"并集: {list(set(a).union(b))}")
    print(f"差集 (b - a): {list(set(b).difference(set(a)))}")
    print(f"差集 (a - b): {list(set(a).difference(set(b)))}")
    print(f"对称差集: {list(set(a).symmetric_difference(b))}")


def main():
    """主函数，运行集合运算示例。"""
    a = [0, 1, 2, 3, 4]
    b = [0, 2, 6]
    
    demonstrate_set_operators(a, b)
    demonstrate_set_methods(a, b)


if __name__ == "__main__":
    main()
