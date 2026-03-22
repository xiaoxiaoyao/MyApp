#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
计算器工具模块
提供基本的数学运算功能，包括四则运算、幂运算、圆面积计算和数据处理。
"""

import math


class Calculator:
    """
    计算器类，封装了常用的数学运算方法。
    
    支持的运算：加法、减法、乘法、除法、幂运算。
    """
    
    def add(self, a: float, b: float) -> float:
        """
        加法运算：计算两个数的和。
        
        Args:
            a (float): 第一个加数
            b (float): 第二个加数
        
        Returns:
            float: 两个数的和
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        减法运算：计算两个数的差（a - b）。
        
        Args:
            a (float): 被减数
            b (float): 减数
        
        Returns:
            float: 两个数的差
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        乘法运算：计算两个数的乘积。
        
        Args:
            a (float): 第一个因数
            b (float): 第二个因数
        
        Returns:
            float: 两个数的乘积
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        除法运算：计算两个数的商（a / b）。
        
        Args:
            a (float): 被除数
            b (float): 除数
        
        Raises:
            ValueError: 当除数b为0时抛出异常
        
        Returns:
            float: 两个数的商
        """
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """
        幂运算：计算base的exponent次方。
        
        Args:
            base (float): 底数
            exponent (float): 指数
        
        Returns:
            float: base^exponent 的结果
        """
        return math.pow(base, exponent)


def calculate_area(radius: float) -> float:
    """
    计算圆的面积。
    
    使用标准库math.pi作为圆周率，精度更高。
    
    Args:
        radius (float): 圆的半径
    
    Returns:
        float: 圆的面积，公式：π * radius^2
    """
    area = math.pi * radius * radius
    return area


def process_data(data_list: list[float]) -> list[float]:
    """
    处理数字列表：对列表中的每个元素进行转换。
    
    转换规则：
    - 正数 → 乘以2
    - 非正数 → 替换为0
    
    Args:
        data_list (list[float]): 待处理的数字列表
    
    Returns:
        list[float]: 处理后的结果列表
    """
    result = []
    for i in data_list:
        if i > 0:
            result.append(i * 2)
        else:
            result.append(0)
    return result
