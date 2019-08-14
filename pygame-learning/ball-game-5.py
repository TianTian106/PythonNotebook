#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 00:16:16 2019

@author: tiantian

1. 色彩机制
    Pygame.Color : 色彩表达
        Color类用于表达色彩，使用RGB或RGBA色彩模式。A为不透明度，可选
        Color类可以用色彩名字、RGBA值、HTML色彩格式等方式定义
        Color(name) : Color('grey')
        Color(r,g,b,a) : Color(190, 190, 190, 255)
        Color(rgbvalue) : Color('#BEBEBEFF')
        pygame.Color.r : 红色值
        pygame.Color.g : 绿色值
        pygame.Color.b : 蓝色值
        pygame.Color.a : alpha值
        pygame.Color.normalize : 将RGBA各通道值归一到0-1之间
2. 图形绘制机制


"""

import pygame
import sys


def rgb_channel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))


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
    pygame.display.set_caption('ball game 5', 'ball game')
    ball = pygame.image.load('PYG02-ball.gif')  # Surface 对象（图像）
    ballrect = ball.get_rect()  # Rect 对象（覆盖图像的外切矩形）
    fps = 300  # Frames per Second 每秒帧率参数，视频中每次展示的静态图像称为帧。
    fclock = pygame.time.Clock()  # Clock 对象，用于操作时间
    still = False  # 标注小球是静止还是移动
    bgcolor = pygame.Color('black')
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
        # R：水平距离/窗体宽度 取值0-255
        bgcolor.r = rgb_channel(ballrect.left * 255 / width)
        # G：垂直距离/窗体高度 取值0-255
        bgcolor.g = rgb_channel(ballrect.top * 255 / height)
        # B：水平和垂直速度差别，最小速度/最大速度 取值0-255
        bgcolor.b = rgb_channel(min(speed[0], speed[1]) * 255 / max(speed[0], speed[1], 1))
        # 窗口刷新部分
        screen.fill(bgcolor)  # 图片移动走后系统默认填充白色
        screen.blit(ball, ballrect)  # 将ball绘制到ballrect位置上。通过Rect对象引导绘制。
        pygame.display.update()  # pygame.display 控制屏幕
        fclock.tick(fps)  # 控制帧速度，即窗口刷新速度。
