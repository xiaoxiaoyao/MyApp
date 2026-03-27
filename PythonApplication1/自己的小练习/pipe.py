#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
管道通信示例程序
使用 Unix 管道进行进程间通信计算圆周率

管道是 Unix 进程间通信最常用的方法之一，它通过在父子进程之间
开通读写通道来进行双工交流。我们通过 os.read() 和 os.write()
来对文件描述符进行读写操作，使用 os.close() 关闭描述符。
"""

import os
import sys
import math


def slice_calculation(mink, maxk):
    """计算指定范围内的累加和。

    Args:
        mink (int): 起始索引
        maxk (int): 结束索引

    Returns:
        float: 累加和
    """
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k + 1) / (2 * k + 1)
    return s


def calculate_pi(n):
    """使用多进程和管道计算圆周率。

    Args:
        n (int): 计算精度

    Returns:
        float: 计算出的圆周率值

    Note:
        此函数仅在 Unix/Linux 系统上可用，因为 Windows 内核中没有 os.fork() 函数
    """
    child_processes = {}
    unit = n / 10

    for i in range(10):
        mink = int(unit * i)
        maxk = int(mink + unit)
        read_fd, write_fd = os.pipe()
        pid = os.fork()

        if pid > 0:
            child_processes[pid] = read_fd
            os.close(write_fd)
        else:
            os.close(read_fd)
            result = slice_calculation(mink, maxk)
            os.write(write_fd, str(result).encode())
            os.close(write_fd)
            sys.exit(0)

    sums = []
    for pid, read_fd in child_processes.items():
        sums.append(float(os.read(read_fd, 1024)))
        os.close(read_fd)
        os.waitpid(pid, 0)

    return math.sqrt(sum(sums) * 8)


def main():
    """主函数，运行圆周率计算。"""
    print(calculate_pi(10000000))


if __name__ == "__main__":
    main()
