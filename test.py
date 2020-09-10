from collections import deque
import random
import numpy as np
import wave
import pygame
def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100
    N =  int(sampleRate/freq)

    #initialize ring buffer
    buf = deque([random.random()-0.5 for i in range(N)])  #【-0.5，0.5】随机数生产deque

    samples = np.array([0]*nSamples,'float32')  #建立浮点数组来报错声音采样
    for i in range(nSamples):
        samples[i] = buf[0] #第一个随机数呗复制到采样缓冲区
        #低通滤波器
        avg = 0.996*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
        samples = np.array(samples*32767,'init16')  #转换为16位带符号的整数
        return samples.tostring() #转换为字符串写入wave



def writeWAVE(fname,data):
    '''写入wav文件'''
    file = wave.open(fname,'wb') #创建一个wav文件

    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100

    file.setparams((nChannels,sampleWidth, frameRate, nFrames,'NONE','noncompressed'))#单声道、16位，无压缩、
    file.writeframes(data)#将数据写入
    file.close()

class NotePlayer:
    '''播放wav文件'''
    def __init__(self):
        pygame.mixer.pre_init(44100,-16,1,2048)#初始化mixer类采样率、16位、单声道、缓冲区
        pygame.init()
        self.notes = {}  #创建一个音符字典

    def add(self,fileName):
        self.notes[fileName] = pygame.mixer.Sound(fileName)

    def play(self,fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName+'not found!')
    def playRandom(self):
        index = random.randint(0,len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()