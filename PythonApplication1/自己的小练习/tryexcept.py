#!/usr/bin/env python3
import sys

def test_try_except():
    """测试异常处理功能
    
    Returns:
        str: 执行成功的消息
    """
    try:
        # 模拟正常情况
        i = int("10")
        return '执行成功'
    except Exception as err:
        print('ERROR', err)
        return '执行失败'
    finally:
        print("Goodbye!")

if __name__ == "__main__":
    s=input("input your age:")  
    
    try:  
        i=int(s)  
    except Exception as err:  
        print('ERROR',err)  
    finally:  
        print("Goodbye!") 

