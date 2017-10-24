#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
加减乘除4个函数的单元测试
https://docs.python.org/3/library/unittest.html
'''

class ZeroMultiError(Exception):
    '''
    测试注释一自定义一个错误类型，乘以0为错误
    '''
    pass

def add(a=0, b=0):
    '''
    测试注释一这就是加法
    '''
    return a+b

def minus(a, b):
    '''
    测试注释一这就是减法
    '''
    return a-b

def multi(a, b):
    '''
    测试注释一这就是乘法
    '''
    return a*b

def multiNotZero(a, b):
    '''
    测试注释一这是一个特殊的乘法，乘数不能为0
    '''
    if a == 0 or b == 0:
        raise ZeroMultiError('multi',[a,b])
    return a*b

def divide(a, b):
    '''
    测试注释一这是除法，注意除数不能为0
    '''
    if b == 0:
        raise ZeroDivisionError('divide',b)
    return a/b

import unittest

class TestMathFunc(unittest.TestCase):
    '''Test mathfuc.py'''
    def setUp(self):
        '''开始测试时使用setUp设置环境，注意每个测试用例都会跑一遍'''
        print('unittest start')
        a, b = 0, 0

    def tearDown(self):
        '''结束测试时使用tearDown清理环境，注意每个测试用例都会跑一遍'''
        print('unittest ended')

    def test_add(self):
        '''Test method add(a, b)'''
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        '''Test method minus(a, b)'''
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        '''Test method multi(a, b)'''
        self.assertEqual(6, multi(2, 3))

    def test_multiNotZero(self):
        '''Test method multi(a, b)'''
        self.assertEqual(6, multiNotZero(2, 3))

    def test_divide(self):
        '''Test method divide(a, b)'''
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

    def test_divide_error(self):
        '''Test method divide(a, b) when 5 divide 0'''
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_multiNotZero_error(self):
        '''Test method multi(0,0)'''
        with self.assertRaises(ZeroMultiError):
            multiNotZero(5, 0)
            multiNotZero(0, 0)
            multiNotZero(0, 5)
    
    @unittest.skip("demonstrating skipping") # skip掉的测试永不运行
    def test_nothing(self):
        self.fail("shouldn't happen")

if __name__ == '__main__':
    unittest.main()
