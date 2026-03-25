#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环语句示例程序
对比 for 循环和 while 循环的使用方式
"""


def demonstrate_for_loop(counter_list):
    """演示 for 循环的使用。

    Args:
        counter_list (list): 要遍历的列表
    """
    print('''
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

if you use for
it will be:''')
    for item in counter_list:
        print(item)
        if item == 5:
            item = counter_list[8]
        print(item)


def demonstrate_while_loop(counter_list):
    """演示 while 循环的使用。

    Args:
        counter_list (list): 要遍历的列表
    """
    print('''
you should use while
it will be:''')
    i = 0
    length = len(counter_list)
    while i < length:
        print(counter_list[i])
        if i == 5:
            i = counter_list[8]
        print(counter_list[i])
        i += 1


def main():
    """主函数，运行循环语句演示。"""
    counter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    demonstrate_for_loop(counter)
    demonstrate_while_loop(counter)


if __name__ == "__main__":
    main()
