import turtle
import PIL
import fractions
import sys, random , argparse
import numpy as np
import math
import random
from PIL import Image
from datetime import datetime
from fractions import gcd
class Spiro:
    def __init__(self, xc , yc, col, R, r, l):
        #create the turtle object 创建对象
        self.t = turtle.Turtle()
        #设置光标样式为海龟
        self.t.shape('turtle')
        #设置绘图角度增量为5度
        self.step = 5
        #设置一个标志会产生螺旋线
        self.drawingComplete = False
        #帮助初始化spiro对象
        self.setparams(xc, yc, col, R, r, l)
        # 让他准备好重画。
        self.restart()

    def setparams(self,xc,yc,col,R,r,l):
        '''设置的参数。帮助初始化spiro对象'''
        #保存曲线中心的坐标
        self.xc = xc
        self.yc = yc
        #保存圆的半径为整数
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        #使用内置gcd方法来计算半径的GCD
        gcdVal = fractions.gcd(self.r, self.R)
        #保存为nRot
        self.nRot = self.r
        self.k = r/float(R)
        self.t.color(*col)
        # 保存当前的角度
        self.a = 0


    def restart(self):
        '''重置spiro对象的绘制参数'''
        self.drawingComplete = False   #用来追踪某个特定的螺旋线是否完成
        self.t.showturtle() #显示海龟光标
        self.t.up() #抬起笔
        R, k, l = self.R, self.k, self.l #一些局部变量
        a = 0.0
        #计算角度a设置为0时的X\Y坐标，以获得曲线的起点
        x = R*((l-k)*math.cos(a)+l*k*math.cos((l-k)*a/k))
        y = R*((l-k)*math.sin(a)-l*k*math.sin((l-k)*a/k))
        # 笔头移动到此
        self.t.setpos(self.xc+x, self.yc + y)
        # 笔头下落
        self.t.down()

    def draw(self):
        # 用连续的先对绘制该曲线
        R, k, l = self.R, self.k, self.l
        for i in range(0,360*self.nRot+1, self.step):    #它以度表示
            a = math.radians(i)  #将角度转换为弧度
            # 计算参数i的每个XY坐标
            x = R*((l-k)*math.cos(a)+ l*k*math.cos((l-k)*a/k))
            y = R*((l-k)*math.sin(a) - l*k*math.sin((l-k)*a/k))
            self.t.setpos(self.xc+x, self.yc +y)
        # 隐藏小乌龟
        self.t.hideturtle()

    def update(self):
        #如果完成了则跳过其余的步骤  创建动画
        if self.drawingComplete:   #检查标志是否设置，如果没有设置，则执行其余部分
            return
        self.a += self.step   #增加当前角度
        R,k,l = self.R,self.k,self.l
        a = math.radians(self.a)
        x= self.R*((l-k)*math.cos(a) + l*k*math.cos((l-k)*a/k))
        y = self.R*((l-k)*math.sin(a) - l*k*math.sin((l-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        #如果达到了完整范围，绘制完成，隐藏光标
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            self.t.hideturtle()
class SpiroAnimator:
    '''绘制水机的螺线，使用了一个计时器'''
    def __init__(self, N):
        self.deltaT = 10  #十毫秒定时
        #设置保存海龟窗口尺寸
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        for i in range(N):
            rparams = self.genRandomParams()
            spiro = Spiro(*rparams )
            self.spiros.append(spiro)
            turtle.ontimer(self.update,self.deltaT)

    def update(self):
        nComplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawingComplete:
                nComplete += 1
        if nComplete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)
