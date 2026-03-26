#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试运行脚本

运行 TDD 目录下的所有测试用例，并生成测试报告。
"""

import unittest
import sys
import os
import time

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def run_test_file(test_file):
    """运行单个测试文件
    
    Args:
        test_file: 测试文件名
        
    Returns:
        tuple: (成功数, 失败数, 错误数)
    """
    print(f"\n{'='*70}")
    print(f"运行测试: {test_file}")
    print('='*70)
    
    try:
        # 导入测试模块
        module_name = test_file[:-3]  # 去掉 .py
        module = __import__(module_name)
        
        # 创建测试套件
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # 查找所有测试类
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                suite.addTests(loader.loadTestsFromTestCase(obj))
        
        # 运行测试
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        success = result.testsRun - len(result.failures) - len(result.errors)
        failures = len(result.failures)
        errors = len(result.errors)
        
        return success, failures, errors
        
    except Exception as e:
        print(f"运行测试文件 {test_file} 时出错: {e}")
        return 0, 0, 1


def main():
    """主函数"""
    print("\n" + "="*70)
    print("开始运行所有测试")
    print("="*70)
    
    # 获取 TDD 目录下的所有测试文件
    tdd_dir = os.path.dirname(os.path.abspath(__file__))
    test_files = [f for f in os.listdir(tdd_dir) if f.startswith('test_') and f.endswith('.py')]
    
    if not test_files:
        print("未找到测试文件")
        return
    
    print(f"\n发现 {len(test_files)} 个测试文件:")
    for f in test_files:
        print(f"  - {f}")
    
    # 运行所有测试
    total_success = 0
    total_failures = 0
    total_errors = 0
    total_tests = 0
    
    start_time = time.time()
    
    for test_file in sorted(test_files):
        success, failures, errors = run_test_file(test_file)
        total_success += success
        total_failures += failures
        total_errors += errors
        total_tests += success + failures + errors
    
    end_time = time.time()
    duration = end_time - start_time
    
    # 输出总体统计
    print("\n" + "="*70)
    print("总体测试统计")
    print("="*70)
    print(f"  测试文件数: {len(test_files)}")
    print(f"  总测试数: {total_tests}")
    print(f"  通过数: {total_success}")
    print(f"  失败数: {total_failures}")
    print(f"  错误数: {total_errors}")
    print(f"  通过率: {total_success/total_tests*100:.2f}%")
    print(f"  运行时间: {duration:.2f} 秒")
    print("="*70)
    
    # 返回退出码
    if total_failures == 0 and total_errors == 0:
        print("\n✅ 所有测试通过！")
        return 0
    else:
        print("\n❌ 部分测试未通过")
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
