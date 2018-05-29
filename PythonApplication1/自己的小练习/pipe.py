# coding: utf-8

# 管道是Unix进程间通信最常用的方法之一，它通过在父子进程之间开通读写通道来进行双工交流。我们通过os.read()和os.write()来对文件描述符进行读写操作，使用os.close()关闭描述符。

import os
import sys
import math

def slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0/(2*k+1)/(2*k+1)
    return s


def pi(n):
    childs = {}
    unit = n / 10
    for i in range(10):  # 分10个子进程
        mink = unit * i
        maxk = mink + unit
        r, w = os.pipe()
        pid = os.fork() # 切记:windows内核中没有os.fork()函数
        if pid > 0:
            childs[pid] = r  # 将子进程的pid和读描述符存起来
            os.close(w)  # 父进程关闭写描述符，只读
        else:
            os.close(r)  # 子进程关闭读描述符，只写
            s = slice(mink, maxk)  # 子进程开始计算
            os.write(w, str(s))
            os.close(w)  # 写完了，关闭写描述符
            sys.exit(0)  # 子进程结束
    sums = []
    for pid, r in childs.items():
        sums.append(float(os.read(r, 1024)))
        os.close(r)  # 读完了，关闭读描述符
        os.waitpid(pid, 0)  # 等待子进程结束
    return math.sqrt(sum(sums) * 8)


print(pi(10000000))