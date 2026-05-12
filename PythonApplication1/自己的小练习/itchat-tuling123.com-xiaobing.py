#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信自动聊天机器人程序
自动把各种聊天内容发给微软小冰，附带图灵机器人和小冰聊天功能
作者：小尧
"""
import requests
import time
import random
import itchat
from typing import Optional, Dict

# 自动把各种聊天内容发给微软小冰的小程序（附带图灵机器人和小冰聊天）
is_tuling: bool = True
is_xiaobing_chat: bool = True


def get_response(msg: str) -> Optional[str]:
    """获取图灵机器人的回复

    Args:
        msg: 用户输入的消息

    Returns:
        图灵机器人的回复内容，如果请求失败则返回 None
    """
    url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '75137612d89c42f0b9d7a3f5133ec656',  # 这个key可以直接拿来用，随便用，无所谓，放心公开
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(url, data=data).json()
        return r.get('text')
    except Exception:
        return None


# @itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg: Dict) -> str:
    """获取图灵机器人的回复消息

    Args:
        msg: 微信消息对象

    Returns:
        图灵机器人的回复内容，如果请求失败则返回默认回复
    """
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b，
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    return reply or 'I received: ' + msg.get('Text')


# 微信好友发来的内容isFriendChat=True, 群聊发来的内容isGroupChat=True, 公众号发来的内容isMpChat=False
is_friend_chat: bool = True
is_group_chat: bool = True
is_mp_chat: bool = False


@itchat.msg_register(itchat.content.TEXT, isFriendChat=is_friend_chat, isGroupChat=is_group_chat, isMpChat=is_mp_chat)
def xiaobing(msg: Dict) -> None:
    """处理微信消息并转发给小冰

    Args:
        msg: 微信消息对象
    """
    xiaobing_username = itchat.search_mps(name='小冰')[0]['UserName']
    # 发送图灵机器人回复内容
    if is_tuling:
        time.sleep(random.random() * 2)
        itchat.send(tuling_reply(msg), toUserName=xiaobing_username)
    # 发送之前的内容
    if is_xiaobing_chat:
        time.sleep(random.random() * 3)
        itchat.send(msg['Content'], toUserName=xiaobing_username)
    # 对象的别名被显式的销毁，引用计数值为0，等待垃圾回收。
    # 该释放的变量及时释放，如果不及时释放，长期积累占用内存
    del msg


if __name__ == '__main__':
    itchat.auto_login()  # 命令行则 enableCmdQR=2
    itchat.run()
