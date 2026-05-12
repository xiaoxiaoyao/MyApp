#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异步 IO 示例程序
演示 Python 3.5+ 的 asyncio 异步编程特性
在同一个线程里并行执行多个异步任务
"""

import time
import datetime
import asyncio


async def async_task(task_id, *args, **kw):
    """异步任务函数，演示异步执行。

    Args:
        task_id: 任务标识符
        *args: 位置参数
        **kw: 关键字参数
    """
    print(datetime.datetime.now(), ' Hello once! , run now_a= await asyncio.sleep(1) ,async_id=', task_id)
    await asyncio.sleep(1)
    print(datetime.datetime.now(), ' Hello twice! , run time.sleep(1) ,async_id=', task_id)
    time.sleep(1)
    print(datetime.datetime.now(), ' Hello thrice! , run again now_a= await asyncio.sleep(1) ,async_id=', task_id)
    await asyncio.sleep(1)
    print(datetime.datetime.now(), 'hello four times! , now return ,async_id=', task_id)


def test_async():
    """测试异步模块的函数，仅返回True."""
    return True


def main():
    """主函数，运行多个异步任务。"""
    print(datetime.datetime.now())
    print('''
run 

run=[async_now(x) for x in range(0,7)]
loop = asyncio.get_event_loop()

''')
    tasks = [async_task(x) for x in range(0, 7)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()
