#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中秋节微信自动祝福发送程序
使用 itchat 库自动给微信好友发送中秋节祝福
作者：小尧
"""
import itchat
import time
import random
from typing import List, Dict


# 群发内容（随机选一条）
SINCERE_WISH: List[str] = [
    '祝中秋快乐',
    '中秋快乐呀',
    '中秋快乐哟',
    '中秋节快乐呀~',
    '中秋节快乐!',
    '中秋国庆快乐!'
]


def send_festival_greetings(start_index: int = 1) -> None:
    """发送节日祝福给微信好友

    Args:
        start_index: 从第几个好友开始发送，默认从第1个（索引1）开始
    """
    itchat.auto_login(True)
    friend_list: List[Dict] = itchat.get_friends(update=True)[start_index:]

    print(f'即将给 {len(friend_list)} 个好友发送中秋祝福，祝福内容为以下随机挑一个：\n{SINCERE_WISH}')

    i = 1
    for friend in friend_list:
        send_wish: str = random.choice(SINCERE_WISH)
        try:
            # 如果是演示目的，把下面的 itchat.send 方法改为 print 即可
            itchat.send(send_wish, friend['UserName'])
            print(f"{friend['UserName']}，第 {i} 个好友已经成功发送，发送内容为：{send_wish}")
            # print(friend['DisplayName'] or friend['NickName'])
            # 为了防止封号，自动延时发送
            time.sleep(1 + random.random() * 124)
        except Exception as e:
            print(f"ERROR!\n第 {i} 个好友发送失败，以下是详细信息：{friend}")
            print(f"{type(e).__name__}: {e}")
        finally:
            i += 1


if __name__ == "__main__":
    send_festival_greetings()
