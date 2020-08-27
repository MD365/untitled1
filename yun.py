#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, argparse
import sys,os
from matplotlib import pyplot
import plistlib
import  numpy as np

# 获取重复 的曲目
def finUplicates(fileName):
    #read in a play list读取列表
    # plist  = plistlib.readPlist(fileName) #返回文件的顶层字典
    plist = plistlib.load(fileName)
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
    f = open("dups.txt", "w",encoding='utf-8')
    for val in dups:
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()
#查找多个列表中共同的乐谱音轨
def findCommonTracks(fileNames):
    trackNameSets = []
    for filename in fileNames:
        trackNames = set()
        plist = plistlib.load(filename)#返回文件字典
        tracks = plist['Tracks']
        for trackId,track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass
    trackNameSets.append(trackNames)
    commonTracks = set.intersection(*trackNameSets)
    if len(commonTracks)>0:
      f = open("common.txt","w")
      for val in commonTracks:
        s = "%s\n" % val
        f.write(s.encode('utf-8'))
      f.close()
      print("%d common tracks found."
              "track names written to common.txt" % len(commonTracks))
    else:
         print("no common tarcks")

#收集统计信息
def plotStats(fileName):
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    ratings = []  #评分
    durations = []#时长

    for trackId,track in tracks.items():
        try:
            ratings.append(track["Album Rating"])
            durations.append(track['Total Time'])
        except:
            pass
    if ratings == [] or durations ==[]:
        print("no valid album rating/total time data in %s"  % fileName)
        return

# 绘制数据
# x = np.array(durations, np.int32)

if __name__=='__main__':
    trackNames = set()
    print (type(trackNames))