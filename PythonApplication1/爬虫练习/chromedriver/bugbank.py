#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BugBank 网站自动化脚本
用于测试 BugBank 网站的注册功能

注意事项：
1. 敏感信息（如 API Key）已从代码中移除，请通过环境变量设置
2. 添加了完整的文档字符串和注释
3. 修复了格式问题，使用 4 个空格缩进
"""

import os
import random
import time
import requests
import leancloud
from leancloud import Object, LeanCloudError, Query


class BugBankTester:
    """
    BugBank 网站测试器
    
    功能：
    - 自动化测试 BugBank 注册功能
    - 记录测试结果到 LeanCloud
    - 处理各种 HTTP 状态码
    
    配置说明：
    1. 设置环境变量 LEANCLOUD_APP_ID 和 LEANCLOUD_APP_KEY
    2. 或修改下面的配置变量
    """
    
    # 从环境变量获取敏感信息（安全做法）
    LEANCLOUD_APP_ID = os.getenv("LEANCLOUD_APP_ID", "")
    LEANCLOUD_APP_KEY = os.getenv("LEANCLOUD_APP_KEY", "")
    
    # 如果环境变量未设置，可以在这里配置（不推荐）
    # 注意：硬编码敏感信息不安全，仅用于测试
    if not LEANCLOUD_APP_ID:
        LEANCLOUD_APP_ID = ""  # 请从环境变量设置
    if not LEANCLOUD_APP_KEY:
        LEANCLOUD_APP_KEY = ""  # 请从环境变量设置
    
    def __init__(self):
        """初始化测试器"""
        if not self.LEANCLOUD_APP_ID or not self.LEANCLOUD_APP_KEY:
            print("警告: LeanCloud 配置未设置，请设置环境变量")
            print("设置方法: export LEANCLOUD_APP_ID='your_app_id'")
            print("         export LEANCLOUD_APP_KEY='your_app_key'")
        
        # 初始化 LeanCloud
        leancloud.init(self.LEANCLOUD_APP_ID, self.LEANCLOUD_APP_KEY)
        
        # 请求头配置
        self.headers = {
            'Host': 'www.bugbank.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US, zh; q=0.8, zh-CN; q=0.5, en; q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-client-id': 'user-web',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.bugbank.cn/signup.html',
            'Content-Length': '197',
            'Connection': 'keep-alive'
        }
        
        # 请求 URL
        self.url = 'http://www.bugbank.cn/api/signup'
        
        # 初始化测试对象
        self.test_object = self._create_test_object()
    
    def _create_test_object(self):
        """创建 LeanCloud 测试对象"""
        TestObject = Object.extend('TestObject')
        test_object = TestObject()
        
        try:
            test_object.destroy()
        except:
            pass  # 忽略首次运行的错误
        
        test_object.save()
        test_object.set('headers', self.headers)
        test_object.set('url', self.url)
        
        return test_object
    
    def generate_random_code(self) -> str:
        """
        生成随机验证码
        
        返回：
            str: 16位数字字符串
        """
        return '%016d' % random.randint(0, 1000000000000000)
    
    def post_registration(self, verification_code: str) -> requests.Response:
        """
        提交注册请求
        
        参数：
            verification_code (str): 验证码
        
        返回：
            requests.Response: HTTP响应对象
        """
        data = {
            'name': 'test_user',  # 测试用户名
            'email': 'test@example.com',  # 测试邮箱
            'password': verification_code + verification_code,  # 测试密码
            'code': verification_code  # 验证码
        }
        
        response = requests.post(self.url, data=data, headers=self.headers)
        return response
    
    def process_registration_attempt(self) -> int:
        """
        处理单次注册尝试
        
        返回：
            int: 状态码
                0 - 失败（无效验证码或其他错误）
                1 - 成功
        """
        verification_code = self.generate_random_code()
        response = self.post_registration(verification_code)
        status_code = response.status_code
        
        current_time = time.asctime()
        print(f"{current_time} 状态码: {status_code}")
        
        time.sleep(10)  # 避免请求过于频繁
        
        try:
            self.test_object.save()
        except LeanCloudError as error:
            print(f"保存到 LeanCloud 失败: {error}")
        
        # 处理不同的状态码
        if status_code in [406, 409, 429, 504]:
            # 406: 失效邀请码, 409: 冲突, 429: 请求过多, 504: 网关超时
            output = f"状态码 {status_code} - 验证码: {verification_code}"
            print(output)
            self.test_object.set(verification_code, output)
            return 0
        else:
            output = f"{current_time} 状态码 {status_code} - 响应: {response.content}, 验证码: {verification_code}"
            print(output)
            self.test_object.set(verification_code, output)
            return 1
    
    def run_test_loop(self):
        """
        运行测试循环
        
        功能：
        - 持续测试注册功能
        - 按 Ctrl+C 停止测试
        """
        print("开始 BugBank 注册测试...")
        print("按 Ctrl+C 停止测试")
        
        try:
            while True:
                result = self.process_registration_attempt()
                print()  # 空行分隔每次尝试
                
                if result == 1:
                    print("测试成功，停止测试")
                    break
                    
        except KeyboardInterrupt:
            print("\n测试被用户中断")
        finally:
            # 获取并显示最终的测试对象
            try:
                self.test_object.fetch()
                print("测试对象已更新")
            except Exception as error:
                print(f"获取测试对象失败: {error}")
    
    def cleanup(self):
        """清理资源"""
        try:
            self.test_object.destroy()
            self.test_object.save()
            print("资源清理完成")
        except Exception as error:
            print(f"清理资源时出错: {error}")


def main():
    """主函数"""
    tester = BugBankTester()
    
    try:
        tester.run_test_loop()
    finally:
        tester.cleanup()


if __name__ == '__main__':
    main()