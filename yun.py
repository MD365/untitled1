#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, argparse
import sys,os
from matplotlib import pyplot
import plistlib
import  numpy as np

# 获取重复 的曲目
def finUuplicates(fileName):
    #read in a play list读取列表
    plist  = plistlib.readPlist(fileName) #返回文件的顶层字典
    # plistlibist  = plistlib.load(fileName)
    #get the tracks from the tracks dictionary 从tracks字典中获得tracks
    tracks = plist['Tracks']
    #创建一个曲目名称字典
    trackNames = {}
# iterate through the tracks遍历轨迹
    for trackId , track in tracks.items(): #字典常用的遍历，显示出所有字典内容
        try:#有些乐曲可能没有乐曲名称
            name = track['Name'] #对应的名称
            duration = track['Total Time'] #对应的种时间
            if name in trackNames:
                if duration//1000 == trackNames[name][0]//1000: #与trackName里的时间做对比如果想当
                    count = trackNames[name][1]
                    trackNames[name]=(duration,count+1)
            else:
                trackNames[name] = (duration, 1)
        except:
            pass

    # 提取重复的音轨
    dups = []
    for k , v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1],k))

    if len(dups)>0:
        print("found % d duplicates.track name saved to dup.txt" % len(dups))
    else:
        print("no duplicate tracks found")
    f = open(os.path+"\\dups.txt", "w",encoding='utf-8')
    for val in dups:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()
#查找多个列表中共同的乐谱音轨
# def findCommonTracks(fileNames):
#     trackNameSets = []
#     for filename in fileNames:
#         trackName = set()
#         plist = plistlib.readPlist(filename)#返回文件字典
#         tracks = plist['Tracks']
#         for trackId,track in tracks.items():
            

