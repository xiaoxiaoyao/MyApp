#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则表达式操作示例程序
演示 Python 中 re 模块的基本使用方法
"""

import re


def demo_basic_match():
    """演示基本的正则表达式匹配。"""
    pattern = re.compile(r'hello')
    
    match1 = pattern.match('hello world!')
    match2 = pattern.match('helloo world!')
    match3 = pattern.match('helllo world!')
    
    if match1:
        print(match1.group())
    else:
        print('match1匹配失败！')
    
    if match2:
        print(match2.group())
    else:
        print('match2匹配失败！')
    
    if match3:
        print(match3.group())
    else:
        print('match3匹配失败！')


def demo_url_validation():
    """演示 URL 验证的正则表达式。"""
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    test_urls = [
        'https://www.example.com',
        'http://localhost:8000',
        'ftp://192.168.1.1',
        'invalid-url'
    ]
    
    print("\nURL 验证测试：")
    for url in test_urls:
        is_valid = url_regex.match(url) is not None
        print(f"{url}: {'有效' if is_valid else '无效'}")


def explain_re_flags():
    """解释 re 模块的常用标志参数。"""
    print("\nre 模块标志参数说明：")
    print("re.I (re.IGNORECASE): 忽略大小写")
    print("re.M (re.MULTILINE): 多行模式，改变'^'和'$'的行为")
    print("re.S (re.DOTALL): 点任意匹配模式，改变'.'的行为")


def main():
    """主函数，运行正则表达式示例。"""
    print("正则表达式基本匹配示例：")
    demo_basic_match()
    demo_url_validation()
    explain_re_flags()


if __name__ == "__main__":
    main()
