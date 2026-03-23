#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask 应用配置文件

包含 Flask 应用的基础配置、调试工具配置和网站信息配置。
敏感信息已从代码中移除，使用环境变量管理。
"""

import os


class Config:
    """
    Flask 应用配置类
    
    包含以下配置分组：
    1. Flask 基础配置
    2. 调试工具栏配置
    3. 网站信息配置
    """
    
    # ======================
    # 1. Flask 基础配置
    # ======================
    
    # 服务器监听地址
    HOST = os.getenv('FLASK_HOST', 'localhost')
    
    # 服务器监听端口
    PORT = int(os.getenv('FLASK_PORT', 5000))
    
    # 调试模式开关
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # 会话加密密钥（必须从环境变量设置）
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', '')
    
    # ======================
    # 2. 调试工具栏配置
    # ======================
    # 工具栏文档: http://www.pythondoc.com/flask-debugtoolbar/index.html
    
    # 启用调试工具栏（与 DEBUG 模式同步）
    DEBUG_TB_ENABLED = DEBUG
    
    # 拦截重定向
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    
    # 启用性能分析器
    DEBUG_TB_PROFILER_ENABLED = False
    
    # 启用模板编辑器
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = False
    
    # ======================
    # 3. 网站信息配置
    # ======================
    
    # 网站基本信息字典
    info = {
        'Title': 'Yao',            # 网站标题
        'WebPage': 'Page',         # 页面名称
        'WebName': 'MyFirstWebPython'  # 网站名称
    }
    
    @classmethod
    def validate_security_config(cls) -> bool:
        """
        验证安全相关配置
        
        返回：
            bool: 配置是否安全
                  True - 配置安全
                  False - 存在安全风险
        """
        security_issues = []
        
        # 检查 SECRET_KEY 是否设置
        if not cls.SECRET_KEY:
            security_issues.append("FLASK_SECRET_KEY 未设置，请设置环境变量")
        
        # 检查生产环境是否关闭 DEBUG 模式
        if cls.DEBUG and os.getenv('FLASK_ENV') == 'production':
            security_issues.append("生产环境不应启用 DEBUG 模式")
        
        # 检查是否使用默认密钥
        if cls.SECRET_KEY == 'development key':
            security_issues.append("不应使用默认的 development key")
        
        # 输出安全警告
        if security_issues:
            print("⚠️  安全配置警告:")
            for issue in security_issues:
                print(f"   - {issue}")
            return False
        
        return True
    
    @classmethod
    def get_all_config(cls) -> dict:
        """
        获取所有配置
        
        返回：
            dict: 包含所有配置项的字典
        """
        config_dict = {}
        
        # 添加所有类属性（排除私有属性和方法）
        for key, value in cls.__dict__.items():
            if not key.startswith('_') and not callable(value):
                config_dict[key] = value
        
        return config_dict


# 配置验证（应用启动时检查）
if __name__ == "__main__":
    print("配置验证中...")
    if Config.validate_security_config():
        print("✅ 安全配置检查通过")
    else:
        print("❌ 存在安全配置问题，请修复")
    
    print("\n当前配置:")
    for key, value in Config.get_all_config().items():
        if 'KEY' in key or 'SECRET' in key:
            # 敏感信息部分隐藏
            display_value = str(value)[:4] + "****" if value else "未设置"
            print(f"{key:30} = {display_value}")
        else:
            print(f"{key:30} = {value}")