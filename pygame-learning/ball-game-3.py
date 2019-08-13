#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:56:52 2019

@author: tiantian

pygame.display 控制屏幕，同一时间只能有一个屏幕
1. 屏幕尺寸和模式：
    pygame.display.set_mode(r = (0, 0), flags = 0) # 设置相关屏幕模式
        r:屏幕分辨率(width, height)。 
        flag:控制显示类型，可用|组合使用，常用：
            pygame.RESIZABLE   窗口大小可调（尺寸变化的相应）
                pygame.VIDEORESIZE    窗口大小更改的事件，返回event.size元组，包含新窗口的宽度和高度（仅事件发生时有用）
                    宽度：.size[0], event.w
                    高度：.size[1], event.h
            pygame.NOFRAME     窗口没有边界显示（增加程序退出方式，如ESC）
            pygame.FULLSCREEN  窗口全屏显示  
            （注意每种显示方式要配合相应的处理机制）
    pygame.display.Info() # 生成屏幕相关信息
        产生 VideoInfo 对象，表达当前屏幕的参数信息
        在.set_mode()之前调用，则显示当前系统显示参数信息
            current_w：当前显示模式或窗口的像素宽度
            current_h：当前显示模式或窗口的像素高度
2. 窗口标题和图标：
    pygame.display.set_caption(title, icontitle = None) # 设置标题信息
        titile：窗口的标题内容
        icontitle：图标化后的小标题（可选，部分操作系统没有）
    pygame.display.set_icon(surface) # 设置图标信息
        图标是一个 Surface 对象
    pygame.display.get_caption() # 获得图标，返回(title, icontitle)
        根据游戏清洁修改标题内容
3. 窗口感知和刷新：
    pygame.display.get_active() # 判断窗口是否被最小化
        当窗口在系统中显示（屏幕绘制/非图标化）时返回True，否则返回False
        最小化后暂停游戏，改变相应模式
    pygame.display.flip()
        速度慢，重新绘制整个屏幕对应的窗口
    pygame.display.update()
        速度快，仅仅绘制窗口中有变化的区域
4. 支持OpenGL和硬件加速（参考官网：www.pygame.org）
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
    pygame.display.set_caption('ball game 3', 'ball game')
    ball = pygame.image.load('PYG02-ball.gif')  # Surface 对象（图像）
    ballrect = ball.get_rect()  # Rect 对象（覆盖图像的外切矩形）
    fps = 300  # Frames per Second 每秒帧率参数，视频中每次展示的静态图像称为帧。
    fclock = pygame.time.Clock()  # Clock 对象，用于操作时间

    while True:
        # 事件处理部分
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                # exit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
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

        if pygame.display.get_active():
            ballrect = ballrect.move(speed[0], speed[1])
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # 窗口刷新部分
        screen.fill(BACKGROUND_RGB)  # 图片移动走后系统默认填充白色
        screen.blit(ball, ballrect)  # 将ball绘制到ballrect位置上。通过Rect对象引导绘制。
        pygame.display.update()  # pygame.display 控制屏幕
        fclock.tick(fps)  # 控制帧速度，即窗口刷新速度。
