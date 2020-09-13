from PIL import Image
import numpy as np
import math
import sys,random,argparse
#定义两种灰度等级
#70个等级的灰度字符
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?_+~<>i!lI;:,\"^`"

gscale2 = "@%#*+=-:. "
cols = 100.0 #自定义列数
scale = 0.43
#打开图像分割成网格

image = Image.open(fileName).convert('L')#打开图像并转换为灰度图像l

W, H = image.sige[0] , image.sige[1]#分别保存了图像的宽度和高度

w = W/cols #根据用户自定的列数cols计算宽度

h = w/scale #计算小块的高度


rows = int(H/h) #计算行数

#计算平均亮度
def getAveragel(image):
    im = np.array(image)#灰度图像生成了一个二维数组
    w,h = im.shape #获取二维数组的行和列
    return np.average(im.reshape(w*h))#先将二维数组变为一维然后取平均值

#从图像生成ASCII
aimg=[]
for j in range(rows):
    y1 = int(j*h)
    y2 = int((j+1)*h)
    if j == rows-1:
        y2 = H
    aimg.append("") #添加空字符
    for i in range(cols):
        x1 = int(i*w)
        x2 = int((i+1)*w)
        if i ==cols -1:
            x2 = w
        img = image.crop((x1,y1,x2,y2))#提取小块根据坐标点
        avg = int(getAveragel(img)) #获取小块的平均亮度
        if moreLevels:
            gsval = gscale1[int((avg*69)/255)]
        else:
            gsval = gscale2[int((avg*9)/255)]
        aimg[j] += gsval

#将字符串写入文件
f = open(outFile,'w')
for row in aimg:
    f.write(row+'\n')
    