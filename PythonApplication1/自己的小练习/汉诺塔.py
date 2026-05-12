#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
汉诺塔问题求解程序
使用递归算法解决汉诺塔问题，并输出移动步骤
"""

# 初始化全局变量
move_count = 0


def hanoi(n, source, auxiliary, target):
    """汉诺塔递归函数，仅输出移动步骤。

    Args:
        n (int): 要移动的圆盘数量
        source (str): 源塔名称
        auxiliary (str): 辅助塔名称
        target (str): 目标塔名称
    """
    if n == 1:
        print(source, '->', target)
    else:
        hanoi(n - 1, source, target, auxiliary)
        print(source, '->', target)
        hanoi(n - 1, auxiliary, source, target)


def is_in_tower(tower, target_disk):
    """检查目标圆盘是否在指定的塔中。

    Args:
        tower (tuple): 塔的元组，包含塔名和圆盘列表
        target_disk (int): 要查找的圆盘编号
    """
    if target_disk in tower[1]:
        print(target_disk, 'in tower', tower[0])


def move_disk(n, source, auxiliary, target, track_disk=None):
    """递归移动汉诺塔圆盘。

    Args:
        n (int): 要移动的圆盘数量
        source (tuple): 源塔
        auxiliary (tuple): 辅助塔
        target (tuple): 目标塔
        track_disk (int, optional): 需要跟踪的圆盘编号
    """
    global move_count
    if n == 1:
        move_count += 1
        print('#', source[0], '-->', target[0])
        disk = source[1].pop()
        target[1].append(disk)
        if track_disk is not None:
            is_in_tower(source, track_disk)
            is_in_tower(auxiliary, track_disk)
            is_in_tower(target, track_disk)
    else:
        move_disk(n - 1, source, target, auxiliary, track_disk)
        move_count += 1
        print('#', source[0], '-->', target[0])
        disk = source[1].pop()
        target[1].append(disk)
        if track_disk is not None:
            is_in_tower(source, track_disk)
            is_in_tower(auxiliary, track_disk)
            is_in_tower(target, track_disk)
        move_disk(n - 1, auxiliary, source, target, track_disk)


def main():
    """主函数，获取用户输入并执行汉诺塔求解。"""
    # 获取用户输入
    num = int(input('请输入汉诺塔的层数：'))
    track_disk = int(input('请输入感兴趣的层数：'))

    # 检查输入合法性
    if num >= 15:
        print('num is too big')
        return

    # 初始化三个塔
    tower_a = list(range(num))
    tower_a.reverse()
    tower_b = []
    tower_c = []
    a = ('A', tower_a)
    b = ('B', tower_b)
    c = ('C', tower_c)

    # 输出初始状态
    print(a, b, c, 'start program', sep='\n', end='\n')
    print('your tower:', a, b, c)

    # 执行汉诺塔移动
    move_disk(num, a, b, c, track_disk)

    # 输出最终结果
    print('最终结果', a, b, c, sep='\n', end='\n')
    print(f'总移动次数: {move_count}')


if __name__ == "__main__":
    main()
