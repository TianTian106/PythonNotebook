#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:56:52 2019

@author: tiantian
"""

import pygame
import sys

if __name__ == '__main__':
    # 初始化部分
    pygame.init()
    size = width, height = 600, 400
    speed = [1, 1]
    BACKGROUND_RGB = 247, 236, 248
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('ball game 1')
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
        ballrect = ballrect.move(speed[0], speed[1])
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        # 窗口刷新部分
        screen.fill(BACKGROUND_RGB)  # 图片移动走后系统默认填充白色
        screen.blit(ball, ballrect)  # 将ball绘制到ballrect位置上。通过Rect对象引导绘制。
        pygame.display.update()
        fclock.tick(fps)  # 控制帧速度，即窗口刷新速度。