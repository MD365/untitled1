import sys,os
import time.random
import wave,argparse,pygame
import numpy as np
from collections import  deque
from matplotlib import pyplot as plt

gShowPlot = False


# notes of a Pentatonic Minor scale 定义钢琴音符
# piano C4-E(b)-F-G-B(b)-C5
pmNotes = {'C4': 262, 'Eb': 311, 'F': 349, 'G':391, 'Bb':466}

# write out WAVE file 写出wave文件
def wri