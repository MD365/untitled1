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
        #create the turtle object
        self.t = turtle.Turtle()
        #设置光标样式为还贵
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
        '''设置的参数'''
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
        self.drawingComplete = False
        self.t.showturturtle()
