#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目自动化测试运行脚本

运行项目中所有的测试用例，并生成测试报告。

使用方法：
    python run_all_tests.py

特点：
- 自动发现并运行 TDD 目录下的所有测试文件
- 生成详细的测试报告
- 计算测试通过率
- 处理模块导入错误和其他异常
"""

import os
import sys
import subprocess
import time
import json

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# TDD 目录
TDD_DIR = os.path.join(ROOT_DIR, 'TDD')


def run_test_file(test_file):
    """运行单个测试文件
    
    Args:
        test_file: 测试文件名
        
    Returns:
        dict: 测试结果
    """
    print(f"\n{'='*70}")
    print(f"运行测试: {test_file}")
    print('='*70)
    
    try:
        # 运行测试文件
        result = subprocess.run(
            [sys.executable, os.path.join(TDD_DIR, test_file)],
            capture_output=True,
            text=True,
            timeout=30  # 设置30秒超时
        )
        
        # 解析测试结果
        output = result.stdout + result.stderr
        
        # 提取测试统计信息
        success_count = 0
        failure_count = 0
        error_count = 0
        test_count = 0
        
        # 简单的结果解析
        if 'FAILED' in output:
            failure_count = output.count('FAILED')
        if 'ERROR' in output:
            error_count = output.count('ERROR')
        if 'OK' in output:
            success_count = output.count('.')
        
        # 计算测试总数
        test_count = success_count + failure_count + error_count
        
        # 计算通过率
        if test_count > 0:
            pass_rate = (success_count / test_count) * 100
        else:
            pass_rate = 0.0
        
        return {
            'file': test_file,
            'success': success_count,
            'failures': failure_count,
            'errors': error_count,
            'total': test_count,
            'pass_rate': pass_rate,
            'output': output,
            'returncode': result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            'file': test_file,
            'success': 0,
            'failures': 0,
            'errors': 1,
            'total': 1,
            'pass_rate': 0.0,
            'output': '测试执行超时',
            'returncode': -1
        }
    except Exception as e:
        return {
            'file': test_file,
            'success': 0,
            'failures': 0,
            'errors': 1,
            'total': 1,
            'pass_rate': 0.0,
            'output': f'运行错误: {str(e)}',
            'returncode': -1
        }


def main():
    """主函数"""
    print("\n" + "="*70)
    print("项目自动化测试")
    print("="*70)
    print(f"测试时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 获取 TDD 目录下的所有测试文件
    test_files = [f for f in os.listdir(TDD_DIR) if f.startswith('test_') and f.endswith('.py')]
    
    if not test_files:
        print("未找到测试文件")
        return
    
    print(f"\n发现 {len(test_files)} 个测试文件:")
    for f in test_files:
        print(f"  - {f}")
    
    # 运行所有测试
    results = []
    total_success = 0
    total_failures = 0
    total_errors = 0
    total_tests = 0
    
    start_time = time.time()
    
    for test_file in sorted(test_files):
        result = run_test_file(test_file)
        results.append(result)
        
        total_success += result['success']
        total_failures += result['failures']
        total_errors += result['errors']
        total_tests += result['total']
    
    end_time = time.time()
    duration = end_time - start_time
    
    # 计算总体通过率
    if total_tests > 0:
        overall_pass_rate = (total_success / total_tests) * 100
    else:
        overall_pass_rate = 0.0
    
    # 生成测试报告
    print("\n" + "="*70)
    print("测试报告")
    print("="*70)
    
    # 打印每个测试文件的结果
    print("\n详细结果:")
    for result in results:
        print(f"\n{result['file']}:")
        print(f"  测试数: {result['total']}")
        print(f"  通过: {result['success']}")
        print(f"  失败: {result['failures']}")
        print(f"  错误: {result['errors']}")
        print(f"  通过率: {result['pass_rate']:.2f}%")
        if result['errors'] > 0:
            print(f"  错误信息: {result['output'][:200]}...")
    
    # 打印总体统计
    print("\n" + "="*70)
    print("总体统计")
    print("="*70)
    print(f"  测试文件数: {len(test_files)}")
    print(f"  总测试数: {total_tests}")
    print(f"  通过数: {total_success}")
    print(f"  失败数: {total_failures}")
    print(f"  错误数: {total_errors}")
    print(f"  总体通过率: {overall_pass_rate:.2f}%")
    print(f"  运行时间: {duration:.2f} 秒")
    print("="*70)
    
    # 输出状态
    if total_failures == 0 and total_errors == 0:
        print("\n✅ 所有测试通过！")
        return 0
    else:
        print("\n❌ 部分测试未通过")
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
