#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 733: 图像渲染（Flood Fill）
使用深度优先搜索（DFS）实现 flood fill 算法
"""
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    """执行 flood fill 操作

    Args:
        image: 二维数组表示的图像
        sr: 起始行坐标
        sc: 起始列坐标
        new_color: 新颜色值

    Returns:
        渲染后的图像
    """
    old_color = image[sr][sc]
    if old_color == new_color:
        return image
    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int) -> None:
        """深度优先搜索

        Args:
            r: 当前行坐标
            c: 当前列坐标
        """
        if 0 <= r < rows and 0 <= c < cols and image[r][c] == old_color:
            image[r][c] = new_color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    dfs(sr, sc)
    return image


if __name__ == "__main__":
    result = flood_fill(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        sr=1,
        sc=1,
        new_color=2
    )
    print(result)