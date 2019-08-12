#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 00:16:16 2019

@author: tiantian

1. 键盘事件及类型的使用
    pygame.event.KEYDOWN : 键盘按下事件
        返回：
        event.unicode    按键的unicode码（unicode码与平台有关，不推荐使用 ）
        event.key        按键的常量名称
        event.mod        按键修饰符组合值（修饰符的按位或运算）
    pygame.event.KEYUP : 键盘释放事件
        返回：
        event.key        按键的常量名称
        event.mod        按键修饰符组合值（ = KMOD_SHIFT | KMOD_CTRL | KMOD_ALT）

2. 鼠标事件及类型的使用:
    pygame.event.MOUSEMOTION : 鼠标移动事件
        返回：
        event.pos        鼠标当前坐标值(x,y)，相对于窗口左上角
        event.rel        鼠标相对运动距离(X,Y)，相对于上次事件
        event.buttons    鼠标按钮状态(a,b,c)，对应鼠标左、中、右键，按下为1，反之为0
    pygame.event.MOUSEBUTTONUP : 鼠标键释放事件
        返回：
        event.pos        鼠标当前坐标值(x,y)，相对于窗口左上角
        event.button    鼠标释放键编号n，取值0/1/2，分别对应三个键
    pygame.event.MOUSEBUTTONDOWN : 鼠标键按下事件
        返回：
        event.pos        鼠标当前坐标值(x,y)，相对于窗口左上角
        event.button    鼠标按下键编号n（左键为1，右键为3，设备相关）

"""

import pygame,sys


    
if __name__ == '__main__':
    # 初始化部分
    pygame.init()
    icon = pygame.image.load('PYG03-pink-flower.png')
    pygame.display.set_icon(icon)
    vInfo = pygame.display.Info()
    # size = width, height = vInfo.current_w, vInfo.current_h
    size = width, height = 600, 400
    speed = [1, 1]
    BACKGROUND_RGB = 247, 236, 248
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption('ball game 3', 'ball game')
    ball = pygame.image.load('PYG02-ball.gif') # Surface 对象（图像）
    ballrect = ball.get_rect() # Rect 对象（覆盖图像的外切矩形）
    fps = 300 # Frames per Second 每秒帧率参数，视频中每次展示的静态图像称为帧。
    fclock = pygame.time.Clock() # Clock 对象，用于操作时间
    still = False # 标注小球是静止还是移动
    
    while True:
        # 事件处理部分
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                # exit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                '''
                if event.unicode == "":
                    print("[KEYDOWN]:", "#", event.key, event.mod)
                else:
                    print("[KEYDOWN]:", event.unicode, event.key, event.mod)
                '''
                if event.key == pygame.K_LEFT:
                    speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
                elif event.key == pygame.K_RIGHT:
                    speed[0] = speed[0] + 1 if speed[0] >= 0 else speed[0] - 1
                elif event.key == pygame.K_UP:
                    speed[1] = speed[1] + 1 if speed[1] >= 0 else speed[1] - 1
                elif event.key == pygame.K_DOWN:
                    speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
                elif event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.VIDEORESIZE:
                size = width, height = event.size[0], event.size[1]
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    still = True
            elif event.type == pygame.MOUSEBUTTONUP:
                still = False
                if event.button == 1:
                    ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
            
            '''
            elif event.type == pygame.MOUSEMOTION:
                print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
            elif event.type == pygame.MOUSEBUTTONUP:
                print("[MOUSEBUTTONUP]:", event.pos, event.button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
            '''
                
        if pygame.display.get_active() and not still:
            ballrect = ballrect.move(speed[0], speed[1]) # move 参数为运动的相对距离
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        # 窗口刷新部分
        screen.fill(BACKGROUND_RGB) # 图片移动走后系统默认填充白色
        screen.blit(ball, ballrect) # 将ball绘制到ballrect位置上。通过Rect对象引导绘制。
        pygame.display.update() # pygame.display 控制屏幕
        fclock.tick(fps) # 控制帧速度，即窗口刷新速度。