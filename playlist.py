import argparse,re
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


def findCommonTracks(fileNames):
    """
    Find common tracks in given playlist files, and save them
    to common.txt.在给定的播放列表文件中找到共同的轨道，并保存它们
    """
    trackNameSets = []
    for fileName in fileNames:

        trackNames= set() #创建set集合
        plist = plistlib.readPlist(fileName)
        tracks = plist['Tracks']

        for trackId, track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass
        trackNameSets.append(trackNames)
    commonTracks = set.intersection(*trackNameSets) #返回交集

    if len(commonTracks)>0:
        f = open("common.txt",'wb')
        for val in commonTracks:
            s = "%s\n" %val
            f.write(s.encode("utf-8"))
        f.close()
        print("%d comm tracks found ."
              "track names written to common.txt" % len(commonTracks))

    else:
        print("no common tracks")

def plotStart(fileName):
    """
    Plot some statistics by readin track information from playlist.
    通过读取播放列表中的轨迹信息来绘制一些统计数据。
    """
    plist = plistlib.readPlist(fileName)
    tracks = plist['Tracks']
    ratings = []
    durations =[]
    for trackId,track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass

    if ratings == [] or durations == []:
        print("no valid album rating/total time data in %s" % fileName)
        return
    # cross plot
    x = np.array(durations , np.int32)#重新定义了list为int32 ？
    #转换为分钟
    x = x/60000.0
    y = np.array(ratings,np.int32)

    pyplot.subplot(2.11)
    pyplot.plot(x,y,'o')
    pyplot.axis([0,1.05*np.max(x),1,110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('track rating')

    #plot histogram绘制柱状图
    pyplot.subplot(2,1,2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')

    #show plot
    pyplot.show()


def findDuplicates(fileName):
    """
    find duplicate tracks in given playlist.
    在播放列表中找到重复的曲目。
    :param fileName:
    :return:
    """
    print("finding duplicate tracks in %s..." % fileName)
    #read in playlist
    plist = plistlib.readPlist(fileName)
    #get the tracks
    tracks = plist['Tracks']
    trackNames = {}
    #iterate through tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            if name in trackNames:
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)

            else:
                trackNames[name] = (duration,1)
        except:
            pass

    # store duplicates as (name, count) tuples存储重复元组(名称、计数)
    dups = []
    for k,v in trackNames.items():
        if v[1]>1:
            dups.append((v[1],k))
    if len(dups)>0:
        print("found %d duplicates,track name saved to dup.txt"%len(dups))
    else:
        print("no duplicate tracks found")
    f = open("dups.txt",'w')
    for val in dups:
        f.write("[%d] %s\n" %(val[0],val[1]))
# Gather our code in a main() function

def main():
    descStr = """    This program analyzes playlist files (.xml) exported from iTunes."""

