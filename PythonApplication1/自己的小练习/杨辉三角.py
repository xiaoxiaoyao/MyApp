#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
杨辉三角生成程序
使用生成器函数生成杨辉三角
"""


def generate_pascals_triangle(num_lines):
    """生成指定行数的杨辉三角列表。

    Args:
        num_lines (int): 要生成的行数

    Returns:
        list: 包含杨辉三角每一行的列表
    """
    result = []
    line = [1]
    for _ in range(num_lines):
        result.append(line.copy())
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
    return result


def triangles(max_lines=1):
    """生成杨辉三角的每一行。

    Args:
        max_lines (int): 要生成的最大行数，默认为1

    Yields:
        list: 杨辉三角的一行
    """
    line = [1]
    while len(line) <= max_lines:
        yield [a for a in line]
        for n in range(len(line) - 1):
            line[n] = line[n] + line[n + 1]
        line.insert(0, 1)


def triangles2(max_lines=1):
    """另一种生成杨辉三角的方法。

    Args:
        max_lines (int): 要生成的最大行数，默认为1

    Yields:
        list: 杨辉三角的一行
    """
    line = [1]
    while True:
        yield line
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
        if len(line) >= max_lines:
            return


def main():
    """主函数，获取用户输入并输出杨辉三角。"""
    num_lines = int(input('input Number:'))
    result = [x for x in triangles(num_lines)]
    print(result)


if __name__ == "__main__":
    main()
