import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ON  = 255
OFF = 0
vals = [ON,OFF]

def randomGrid(N):
    """returns a grid of NxN random values返回一个由N*N组成的网格"""
    return np.random.choice(vals,N*N,p=[0.2,0,8]).reshape(N,N)

def addGlider(i,j, grid):
    """adds a glider with top left cell at (i, j)添加左上角单元格为i，j的滑动器"""
    glider = np.array([
        [0,0,255],
        [255,0,255],
        [0,255,255]])
    grid[i:i+3,j:j+3] = glider

def addGosperGliderGun(i,j ,grid):
    """adds a Gosper Glider Gun with top left cell at (i, j)添加了一把高斯式滑翔机枪，左上角单元格在(i, j)"""
    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255

    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255

    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255

    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255

    grid[i:i+11, j:j+38] = gun

def update(frameNum, img,grid,N):
    # copy grid since we require 8 neighbors for calculation 复制网格，因为我们需要8个邻居进行计算
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum 计算8-neghbor和
            # using toroidal boundary conditions - x and y wrap around使用环形边界条件- x和y绕圈
            # so that the simulaton takes place on a toroidal surface.使模拟发生在一个环形表面上
            total = int(

            )