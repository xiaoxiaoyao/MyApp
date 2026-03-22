import sys
import random
import numpy as np
import pygame
from pygame.locals import *

def initial():
    global snake_speed_clock,Display,Display_font,Direction,snake_num,Score
    global Cell_Size,Window_Width,Window_Height,Dark,Red,Green,Yellow,Black
    global snake_food,Snake_speed
    Cell_Size=20
    Window_Width = 1000
    Window_Height = 700
    Dark = (80, 80, 80)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Yellow = (255, 255, 0)
    Black = (0, 0, 0)
    Snake_speed = 16
    pygame.init()
    snake_speed_clock = pygame.time.Clock()
    Display = pygame.display.set_mode((Window_Width, Window_Height))
    pygame.display.set_caption('Snake-Play')
    Display_font = pygame.font.Font('freesansbold.ttf', 20)
    Score=0
    Direction = 'RIGHT'
    snake_num = []
    for i in range(16):
        snake_num.append({'x': i,'y': 20})    
    draw_grid()
    snake_food=make_food(snake_num)
    draw_food(snake_food)
    draw_snake(snake_num)
    pygame.display.update()

def check_Key():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def get_direction(key):
    if (key == K_UP):
        Direction = 'UP'
    elif (key == K_LEFT):
        Direction = 'LEFT'
    elif (key == K_RIGHT):
        Direction = 'RIGHT'
    elif (key == K_DOWN):
        Direction = 'DOWN'
    elif (key == K_SPACE):
        Direction = 'SPACE'
    return Direction

def run_direction():
        global Direction,snake_num,snake_food,Score
        for event in pygame.event.get():
            if event.type == QUIT|K_ESCAPE:
                terminate()
            elif event.type == K_ESCAPE:
                terminate()
            elif event.type == KEYDOWN:
                Direction=get_direction(event.key)
        if Direction == 'RIGHT':
            if snake_num[len(snake_num)-1]==snake_food:
                snake_num.append(snake_food)
                snake_food=make_food(snake_num)
                Score=Score+10
            else:
                X=snake_num[len(snake_num)-1]['x']+1
                Y=snake_num[len(snake_num)-1]['y']
                c={'x': X,'y': Y}
                m=snake_num[1:]
                m.append(c)
                snake_num=m
        if Direction == 'LEFT':
            if snake_num[len(snake_num)-1]==snake_food:
                snake_num.append(snake_food)
                snake_food=make_food(snake_num)
                Score=Score+10
                
            else:
                X=snake_num[len(snake_num)-1]['x']-1
                Y=snake_num[len(snake_num)-1]['y']
                c={'x': X,'y': Y}
                m=snake_num[1:]
                m.append(c)
                snake_num=m
        if Direction == 'UP':
            if snake_num[len(snake_num)-1]==snake_food:
                snake_num.append(snake_food)
                snake_food=make_food(snake_num)
                Score=Score+10
            else:
                X=snake_num[len(snake_num)-1]['x']
                Y=snake_num[len(snake_num)-1]['y']-1
                c={'x': X,'y': Y}
                m=snake_num[1:]
                m.append(c)
                snake_num=m
        if Direction == 'DOWN':
            if snake_num[len(snake_num)-1]==snake_food:
                snake_num.append(snake_food)
                snake_food=make_food(snake_num)
                Score=Score+10
            else:
                X=snake_num[len(snake_num)-1]['x']
                Y=snake_num[len(snake_num)-1]['y']+1
                c={'x': X,'y': Y}
                m=snake_num[1:]
                m.append(c)
                snake_num=m    

def make_food(snake_num):
    foods=[]
    for i in range(int(Window_Width/Cell_Size)):
        for j in range(int(Window_Height/Cell_Size)):
            if {'x':i,'y':j} not in snake_num:
                foods.append({'x':i,'y':j})    
    make_food = foods[random.randint(0, len(foods))]
    snake_food = make_food
    return snake_food

def draw_food(snake_food):
    x = snake_food['x'] * Cell_Size
    y = snake_food['y'] * Cell_Size
    appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(Display, Red, appleRect)
    draw_grid()        
    pygame.display.update() 
 
def draw_snake(snake_num):
    for i in range(len(snake_num)):
        x = snake_num[i]['x'] * Cell_Size
        y = snake_num[i]['y'] * Cell_Size
        appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(Display, Green, appleRect)
    draw_grid()        
    pygame.display.update()
 
def draw_score(score):
    Score_Font = pygame.font.Font('freesansbold.ttf', 40)
    Score_Surf = Score_Font.render('Score : '+str(score), True, Yellow)
    Score_Rect = pygame.Rect(400,20,Cell_Size,Cell_Size)
    Display.blit(Score_Surf, Score_Rect)

def draw_grid():
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(Display, Dark, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(Display, Dark, (0, y), (Window_Width, y))

def terminate():
    pygame.quit()
    sys.exit()
 
if __name__ == '__main__':
    initial()
    while True:
        Display.fill(Black)
        run_direction()
        draw_score(Score)
        draw_food(snake_food)
        draw_snake(snake_num)
        pygame.display.update()   
        snake_speed_clock.tick(Snake_speed)