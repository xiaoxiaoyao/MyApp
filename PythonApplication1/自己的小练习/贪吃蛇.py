#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
贪吃蛇游戏
使用 Pygame 库实现的经典贪吃蛇游戏
"""
import sys
import random
from typing import List, Dict, Optional
import pygame
from pygame.locals import *


# Global variables
snake_speed_clock = None
Display = None
Display_font = None
Direction = 'RIGHT'
snake_num: List[Dict[str, int]] = []
Score = 0
Cell_Size = 20
Window_Width = 1000
Window_Height = 700
Dark = (80, 80, 80)
Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Black = (0, 0, 0)
snake_food: Dict[str, int] = {'x': 0, 'y': 0}
Snake_speed = 16


def initialize() -> None:
    """初始化游戏。"""
    global snake_speed_clock, Display, Display_font, Direction, snake_num, Score
    global Cell_Size, Window_Width, Window_Height, Dark, Red, Green, Yellow, Black
    global snake_food, Snake_speed

    pygame.init()
    snake_speed_clock = pygame.time.Clock()
    Display = pygame.display.set_mode((Window_Width, Window_Height))
    pygame.display.set_caption('Snake-Play')
    Display_font = pygame.font.Font('freesansbold.ttf', 20)
    Score = 0
    Direction = 'RIGHT'
    snake_num = []
    for i in range(16):
        snake_num.append({'x': i, 'y': 20})
    draw_grid()
    snake_food = make_food(snake_num)
    draw_food(snake_food)
    draw_snake(snake_num)
    pygame.display.update()


def check_key() -> Optional[int]:
    """检查用户输入。"""
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return None
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    return key_up_events[0].key


def get_direction(key: int) -> str:
    """根据按键获取移动方向。

    Args:
        key: 按键码

    Returns:
        移动方向
    """
    if key == K_UP:
        return 'UP'
    elif key == K_LEFT:
        return 'LEFT'
    elif key == K_RIGHT:
        return 'RIGHT'
    elif key == K_DOWN:
        return 'DOWN'
    elif key == K_SPACE:
        return 'SPACE'
    return Direction


def run_direction() -> None:
    """根据方向移动蛇。"""
    global Direction, snake_num, snake_food, Score
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            Direction = get_direction(event.key)

    head = snake_num[-1]
    new_head = head.copy()

    if Direction == 'RIGHT':
        new_head['x'] += 1
    elif Direction == 'LEFT':
        new_head['x'] -= 1
    elif Direction == 'UP':
        new_head['y'] -= 1
    elif Direction == 'DOWN':
        new_head['y'] += 1

    if new_head == snake_food:
        snake_num.append(snake_food)
        snake_food = make_food(snake_num)
        Score += 10
    else:
        snake_num = snake_num[1:]
        snake_num.append(new_head)


def make_food(snake_body: List[Dict[str, int]]) -> Dict[str, int]:
    """生成食物位置。

    Args:
        snake_body: 蛇的身体坐标

    Returns:
        食物坐标
    """
    foods = []
    for i in range(int(Window_Width / Cell_Size)):
        for j in range(int(Window_Height / Cell_Size)):
            if {'x': i, 'y': j} not in snake_body:
                foods.append({'x': i, 'y': j})
    return foods[random.randint(0, len(foods) - 1)]


def draw_food(food: Dict[str, int]) -> None:
    """绘制食物。

    Args:
        food: 食物坐标
    """
    x = food['x'] * Cell_Size
    y = food['y'] * Cell_Size
    apple_rect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(Display, Red, apple_rect)
    draw_grid()
    pygame.display.update()


def draw_snake(snake_body: List[Dict[str, int]]) -> None:
    """绘制蛇。

    Args:
        snake_body: 蛇的身体坐标
    """
    for segment in snake_body:
        x = segment['x'] * Cell_Size
        y = segment['y'] * Cell_Size
        segment_rect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(Display, Green, segment_rect)
    draw_grid()
    pygame.display.update()


def draw_score(score: int) -> None:
    """绘制分数。

    Args:
        score: 游戏分数
    """
    score_font = pygame.font.Font('freesansbold.ttf', 40)
    score_surf = score_font.render(f'Score : {score}', True, Yellow)
    score_rect = pygame.Rect(400, 20, Cell_Size, Cell_Size)
    Display.blit(score_surf, score_rect)


def draw_grid() -> None:
    """绘制网格。"""
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(Display, Dark, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(Display, Dark, (0, y), (Window_Width, y))


def terminate() -> None:
    """退出游戏。"""
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    initialize()
    while True:
        Display.fill(Black)
        run_direction()
        draw_score(Score)
        draw_food(snake_food)
        draw_snake(snake_num)
        pygame.display.update()
        snake_speed_clock.tick(Snake_speed)