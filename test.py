import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def addGlider(i,j, grid):
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    grid[i:i+3,j:j+3] = glider

grid = np.zeros(1*1).reshape(1,1)

addGlider(1,1,grid)


print(addGlider(1,1,grid))