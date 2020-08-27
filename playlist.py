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

        trackNames= set()
        plist = plistlib.readPlist(fileName)
        tracks = plist['Tracks']

        for trackId, track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass
        trackNameSets.append(trackNames)