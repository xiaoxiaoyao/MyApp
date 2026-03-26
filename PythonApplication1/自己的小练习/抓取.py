﻿﻿﻿﻿﻿﻿﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础网页抓取示例
使用 requests 和 BeautifulSoup 进行网页数据抓取
"""

import requests
import bs4


def fetch_webpage(url):
    """获取指定 URL 的网页内容。

    Args:
        url (str): 要抓取的网页 URL

    Returns:
        requests.Response: 网页响应对象
    """
    response = requests.get(url)
    return response


def parse_links(response):
    """解析网页响应中的链接。

    Args:
        response (requests.Response): 网页响应对象

    Returns:
        list: 匹配的链接元素列表
    """
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.select('div.info-container a[href^=/en/directory/]')
    return links


if __name__ == "__main__":
    target_url = 'http://www.britishchambershanghai.org/en/directory/list?page=6'
    page_response = fetch_webpage(target_url)
    extracted_links = parse_links(page_response)
    print(f'找到 {len(extracted_links)} 个链接')
