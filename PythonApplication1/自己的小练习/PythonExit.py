#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示 Python 中不同退出方式的示例程序

作者：知乎 - 小尧
运行环境：Python 3.7.0+
"""
import os
import sys


def demo_os_exit() -> None:
    """演示 os._exit(n) 的使用
    
    os._exit(n) 直接退出，不抛异常，不执行相关清理工作，
    常用在子进程的退出
    """
    print('run:    os._exit(0) # os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出')
    os._exit(0)


def demo_sys_exit() -> None:
    """演示 sys.exit(n) 的使用
    
    sys.exit(n) 抛出 SystemExit 异常，会执行 finally 块，
    一般主程序中使用此退出
    """
    try:
        sys.exit('run:xiaoyao_sys.exit(4)_知乎：小尧')
    except SystemExit:
        print('except:xiaoyao_sys.exit(4)_知乎：小尧')
    finally:
        print('xiaoyao_sys.exit(4)quit_知乎：小尧')


def demo_quit_exit() -> None:
    """演示 exit()/quit() 的使用
    
    exit()/quit() 抛出 SystemExit 异常，
    一般在交互式shell中退出时使用
    """
    try:
        quit()
    except SystemExit:
        print('except:xiaoyao_exit()_知乎：小尧')
    finally:
        print('xiaoyao_exit()quit_知乎：小尧')


def main() -> None:
    """主函数，运行所有演示"""
    print('演示 os._exit(n):')
    try:
        demo_os_exit()
    except:
        print('except:xiaoyao_os._exit(0)_知乎：小尧')
    finally:
        print('xiaoyao_os._exit(0)quit_知乎：小尧')
    
    print('\n演示 sys.exit(n):')
    demo_sys_exit()
    
    print('\n演示 exit()/quit():')
    demo_quit_exit()
    
    print('\nxiaoyao_能执行到这里？知乎小尧觉得不可能吧？')


if __name__ == "__main__":
    main()
