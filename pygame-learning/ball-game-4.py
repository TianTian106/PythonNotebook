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

3. 事件处理函数：
    pygame 事件队列最多能存储128个事件。队列满时新到事件将被丢弃。
    3.1 处理事件：
        pygame.event.get() : 从事件队列中获得事件列表，即获得所有被队列的事件
            pygame.event.get(type) : 增加参数，获得某类或某些类事件
            pygame.event.get(typelist)
        pygame.event.poll() : 从事件队列中获得一个事件，并从队列中删除。若事件队列为空，返回 event.NOEVENT
        pygame.event.clear() : 从事件队列中删除事件，默认删除所有事件。可增加参数，删除某类或某些类事件
    3.2 操作事件队列：设置缓存事件的类型
        pygame.event.set_blocked(type or typelist) : 控制哪些类型事件不允许被保存到事件队列中
        pygame.event.get_blocked(type) : 判断某个事件类型是否被事件队列所禁止，禁止返回True，否则返回False
        pygame.event.set_allowed(type or typelist) : 控制哪些类型事件允许被保存到事件队列中
    3.3 生成事件：
        pygame.event.post(Event) : 产生一个事件，并将其放入事件队列
            一般用于放置用户自定义事件（pygame.USEREVENT）
            也可以用户放置系统定义事件（如鼠标或键盘等），给定参数
        pygame.event.Event(type, dict) : 创建一个给定类型的事件
            事件的属性和值采用字典类型复制，属性名采用字符串形式
            如果创建已有事件，属性需要一致
"""

import pygame
import sys

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
    pygame.display.set_caption('ball game 4', 'ball game')
    ball = pygame.image.load('PYG02-ball.gif')  # Surface 对象（图像）
    ballrect = ball.get_rect()  # Rect 对象（覆盖图像的外切矩形）
    fps = 300  # Frames per Second 每秒帧率参数，视频中每次展示的静态图像称为帧。
    fclock = pygame.time.Clock()  # Clock 对象，用于操作时间
    still = False  # 标注小球是静止还是移动

    while True:
        # 用户自定义事件：
        # uevent = pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_SPACE, "mod": pygame.KMOD_ALT})
        # pygame.event.post(uevent)
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
            ballrect = ballrect.move(speed[0], speed[1])  # move 参数为运动的相对距离
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
            if width < ballrect.right < ballrect.right + speed[0]:
                speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
            if height < ballrect.bottom < ballrect.bottom + speed[1]:
                speed[1] = - speed[1]

        # 窗口刷新部分
        screen.fill(BACKGROUND_RGB)  # 图片移动走后系统默认填充白色
        screen.blit(ball, ballrect)  # 将ball绘制到ballrect位置上。通过Rect对象引导绘制。
        pygame.display.update()  # pygame.display 控制屏幕
        fclock.tick(fps)  # 控制帧速度，即窗口刷新速度。
