#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 Turtle 库绘制小猪佩奇和其他图形
"""
import turtle as t
import math
from typing import Optional


def draw_peppa_pig(turtle: t.Turtle = t) -> None:
    """绘制小猪佩奇

    Args:
        turtle: Turtle 实例
    """
    turtle.pensize(6)
    turtle.colormode(255)
    turtle.color((255, 155, 192), "pink")
    turtle.setup(840, 500)
    turtle.speed(10)

    # 鼻子
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    turtle.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a -= 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(25)
    turtle.seth(0)
    turtle.fd(10)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0)
    turtle.fd(20)
    turtle.pd()
    turtle.pencolor(255, 155, 192)
    turtle.seth(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()

    # 头
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(41)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(180)
    turtle.circle(300, -30)
    turtle.circle(100, -60)
    turtle.circle(80, -100)
    turtle.circle(150, -20)
    turtle.circle(60, -95)
    turtle.seth(161)
    turtle.circle(-300, 15)
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pd()
    turtle.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.08
            turtle.lt(3)
            turtle.fd(a)
        else:
            a -= 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.end_fill()

    # 耳朵
    turtle.color((255, 155, 192), "pink")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-7)
    turtle.seth(0)
    turtle.fd(70)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 54)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-12)
    turtle.seth(0)
    turtle.fd(30)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 56)
    turtle.end_fill()

    # 眼睛
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-20)
    turtle.seth(0)
    turtle.fd(-95)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.color((255, 155, 192), "white")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-25)
    turtle.seth(0)
    turtle.fd(40)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color("black")
    turtle.pu()
    turtle.seth(90)
    turtle.fd(12)
    turtle.seth(0)
    turtle.fd(-3)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    # 腮
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-95)
    turtle.seth(0)
    turtle.fd(65)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    # 嘴
    turtle.color(239, 69, 19)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(15)
    turtle.seth(0)
    turtle.fd(-100)
    turtle.pd()
    turtle.seth(-80)
    turtle.circle(30, 40)
    turtle.circle(40, 80)

    # 身体
    turtle.color("red", (255, 99, 71))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-20)
    turtle.seth(0)
    turtle.fd(-78)
    turtle.pd()
    turtle.begin_fill()
    turtle.seth(-130)
    turtle.circle(100, 10)
    turtle.circle(300, 30)
    turtle.seth(0)
    turtle.fd(230)
    turtle.seth(90)
    turtle.circle(300, 30)
    turtle.circle(100, 3)
    turtle.color((255, 155, 192), (255, 100, 100))
    turtle.seth(-135)
    turtle.circle(-80, 63)
    turtle.circle(-150, 24)
    turtle.end_fill()

    # 手
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-40)
    turtle.seth(0)
    turtle.fd(-27)
    turtle.pd()
    turtle.seth(-160)
    turtle.circle(300, 15)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(15)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.seth(-10)
    turtle.circle(-20, 90)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(30)
    turtle.seth(0)
    turtle.fd(237)
    turtle.pd()
    turtle.seth(-20)
    turtle.circle(-300, 15)
    turtle.pu()
    turtle.seth(90)
    turtle.fd(20)
    turtle.seth(0)
    turtle.fd(0)
    turtle.pd()
    turtle.seth(-170)
    turtle.circle(20, 90)

    # 脚
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(-75)
    turtle.seth(0)
    turtle.fd(-180)
    turtle.pd()
    turtle.seth(-90)
    turtle.fd(40)
    turtle.seth(-180)
    turtle.color("black")
    turtle.pensize(15)
    turtle.fd(20)
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(40)
    turtle.seth(0)
    turtle.fd(90)
    turtle.pd()
    turtle.seth(-90)
    turtle.fd(40)
    turtle.seth(-180)
    turtle.color("black")
    turtle.pensize(15)
    turtle.fd(20)

    # 尾巴
    turtle.pensize(4)
    turtle.color((255, 155, 192))
    turtle.pu()
    turtle.seth(90)
    turtle.fd(70)
    turtle.seth(0)
    turtle.fd(95)
    turtle.pd()
    turtle.seth(0)
    turtle.circle(70, 20)
    turtle.circle(10, 330)
    turtle.circle(70, 30)


def draw_sunflower(turtle: t.Turtle = t) -> None:
    """绘制太阳花

    Args:
        turtle: Turtle 实例
    """
    turtle.color("red", "yellow")
    turtle.speed(10)
    turtle.begin_fill()
    for _ in range(50):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()


def draw_snake(turtle: t.Turtle = t,
               rad: float = 1500,
               angle: float = 1400,
               length: int = 0,
               neckrad: float = 0) -> None:
    """绘制小蛇

    Args:
        turtle: Turtle 实例
        rad: 圆弧半径
        angle: 圆弧角度
        length: 循环次数
        neckrad: 脖子圆弧半径
    """
    for _ in range(length):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.forward(rad / 2)
    turtle.circle(neckrad, 180)
    turtle.forward(rad / 4)


def draw_star(turtle: t.Turtle = t) -> None:
    """绘制五角星

    Args:
        turtle: Turtle 实例
    """
    turtle.pensize(5)
    turtle.pencolor("yellow")
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-150, -120)
    turtle.color("violet")
    turtle.write("Done", font=('Arial', 40, 'normal'))


def draw_simple_star(turtle: t.Turtle = t) -> None:
    """绘制简单五角星

    Args:
        turtle: Turtle 实例
    """
    for _ in range(5):
        turtle.fd(40)
        turtle.rt(144)


def draw_odd_star(turtle: t.Turtle = t, n: int = 5) -> None:
    """绘制奇数N角星

    Args:
        turtle: Turtle 实例
        n: 角的数量
    """
    for _ in range(n):
        turtle.forward(100)
        turtle.right(180 - 180 / n)


def draw_even_star(turtle: t.Turtle = t, n: int = 6) -> None:
    """绘制偶数N角星

    Args:
        turtle: Turtle 实例
        n: 角的数量
    """
    n1 = int(n / 2)
    a = (180 * (n - 2) / n)
    b = 180 - a
    c = b / 2
    d = 180 - (c * (n / 2 - 1))
    d1 = (d / 180) * math.pi
    c1 = (c / 180) * math.pi
    e = (math.sin(c1) / math.sin(d1)) * 100
    for _ in range(n1):
        turtle.forward(100)
        turtle.left(90)
        turtle.penup()
        turtle.forward(e)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.left(180 - 180 / n1)


def draw_n_star(turtle: t.Turtle = t, n: int = 5) -> None:
    """绘制N角星，自动选择奇偶绘制方法

    Args:
        turtle: Turtle 实例
        n: 角的数量
    """
    if n % 2 == 1:
        draw_odd_star(turtle=turtle, n=n)
    else:
        draw_even_star(turtle=turtle, n=n)


def draw_simple_rectangle(turtle: t.Turtle = t) -> None:
    """绘制简单长方形

    Args:
        turtle: Turtle 实例
    """
    turtle.width(4)
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.pencolor('green')
    turtle.forward(200)
    turtle.right(90)
    turtle.pencolor('blue')
    turtle.forward(100)
    turtle.right(90)


if __name__ == "__main__":
    import time
    while True:
        time.sleep(5)
        t.clear()
        draw_peppa_pig(t)
