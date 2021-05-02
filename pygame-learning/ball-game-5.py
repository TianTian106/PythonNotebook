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

2. 图形绘制机制 : 利用Rect类操作图形/图像等元素
    pygame.draw : 图形绘制后，返回一个矩形Rect类表示该形状
    pygame.Rect : 表达一个矩形区域的类，存储坐标和长度信息。Rect有很多属性和方法。http://www.pygame.org/docs/ref/rect.html
    eg. pygame.draw.rect(Surface, color, Rect, width = 0)
            Surface : 矩形的绘制屏幕
            Color : 矩形的绘制颜色
            Rect : 矩形的绘制区域
            width : 绘制边缘的宽度，默认为0，即填充矩形
    eg. pygame.draw.polygon(Surface, color, pointlist, width = 0) : 绘制多边形
            pointlist : 多边形顶点坐标列表
    eg. pygame.draw.circle(Surface, color, pos, radius, width = 0) : 绘制圆形
            pos : 圆心坐标
            radius : 半径
    eg. pygame.draw.ellipse(Surface, color, Rect, width = 0) : 绘制椭圆形
            Rect : 椭圆形的绘制区域
    eg. pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width = 0) : 绘制椭圆弧形
            start_angle, stop_angle : 弧形绘制起始和结束弧度值，横向右侧为0度
    eg. pygame.draw.line(Surface, color, start_pos, end_pos, width = 1) : 绘制直线
            start_pos, end_pos : 直线的起始和结束坐标
    eg. pygame.draw.lines(Surface, color, closed, pointlist, width = 1) : 绘制连续多线
            closed : 如果为True，起止节点间自动增加封闭直线
            pointlist : 顶点坐标列表
    eg. pygame.draw.aaline(Surface, color, start_pos, end_pos, blend = 1) : 绘制无锯齿线
            blend : 不为0时，与线条所在背景颜色进行混合
    eg. pygame.draw.aalines(Surface, color, closed, pointlist, blend = 1) : 绘制连续无锯齿多线

3. 文字绘制机制 :
    pygame.freetype : 向屏幕上绘制特定字体的文字，是增强方法，需额外引用
    eg. Windows C:\Windows\Fonts (*.ttf, *.ttc)
    pygame.freetype.Font(file, size=0) : 根据字体和字号生成一个 Font 对象，用render*方法绘制具体文字
        file : 字体类型名称或路径（建议使用绝对路径）
        size : 字体的大小
    Font.render_to(surf, dest, text, fgcolor=None, bgcolor=None, rotation=0, size=0) -> Rect
    Font.render(text, fgcolor=None, bgcolor=None, rotation=0, size=0) -> (Surface, Rect)

4. pygame绘制机制原理精髓
"""

import pygame
import sys
import pygame.freetype

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
    # 绘制图形：
    # rect1 = pygame.draw.rect(screen, pygame.Color('green'), (100, 100, 200, 100), 5)
    # rect2 = pygame.draw.rect(screen, pygame.Color('red'), (210, 210, 200, 100), 0)
    # 绘制文字：
    # font1 = pygame.freetype.Font("/Library/Fonts/Songti.ttc", 36)
    # font1Rect = font1.render_to(screen, (200, 160), "世界和平", fgcolor=pygame.Color('yellow'), size=50)
    # f1surf, f1rect = font1.render("世界和平", fgcolor=pygame.Color('yellow'), size=50)
    # screen.blit(f1surf, (200, 160))
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
        fclock.tick(fps)  # 控制帧速度，即窗口刷新速度
