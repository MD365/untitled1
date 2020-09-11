import sys,os
import time,random
import wave,argparse,pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

gShowPlot = False


# notes of a Pentatonic Minor scale 定义钢琴音符
# piano C4-E(b)-F-G-B(b)-C5
pmNotes = {'C4': 262, 'Eb': 311, 'F': 349, 'G':391, 'Bb':466}

# write out WAVE file 写出wave文件
def writeWAVE(fname,data):
    file = wave.open(fname,'wb')
    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100

    file.setparams((nChannels,sampleWidth,frameRate,nFrames,'NONE','noncompressed'))

    file.writeframes(data)
    file.close()

#generate note of given frequency生成给定频率的音符
def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100  #采样率
    N = int(sampleRate/freq)
    # initialize ring buffer 初始化环形缓冲区
    buf = deque([random.random()-0.5 for i in range(N)])   #生成随机数list （+- 0.5)）
    #plot of flag set 标志集图
    if gShowPlot:
        axline, = plt.plot(buf)
    # init sample buffer 示例缓冲区
    samples = np.array([0]*nSamples,'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
        if gShowPlot:
            if i%1000 == 0:
                axline.set_ydata(buf)
                plt.draw()
    samples = np.array(samples * 32767,'init16')
    return samples.tostring()

class NotePlayer:
    def __init__(self):
        pygame.mixer.pre_init(44100.-16,1,2048)
        pygame.init()
        self.notes = {}
    def add(self,fileName):
        self.notes[fileName]= pygame.mixer.Sound(fileName)
    def play(self,fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName+'not found')
    def playRandom(self):
        index = random.randint(0,len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()

def main():
    global gShowPlot

    parser = argparse.ArgumentParser(description="Generating sounds with Karplus String Algorithm.")

    parser.add_argument('--display',action='store_true',required=False)
    parser.add_argument('--play',action='store_true',required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    args = parser.parse_args()

    if args.display:
        gShowPlot = True
        plt.ion()

    nplayer = NotePlayer()
    print('creation notes...')
    for name, freq in list(pmNotes.items()):  #定义音节
        fileName = name +'.wav'
        if not os.path.exists(fileName) or args.display:
            data = generateNote(freq) #将音节转化为音符
            print('creating'+fileName+',,,')
            writeWAVE(fileName,data)   #写出wave文件
        else:
            print('filename already created.skipping')

        nplayer.add(name+'.wav')

        if args.display:
            nplayer.play(name+'.wav')
            time.sleep(0.5)

    if args.play:
        while True:
            try:
                nplayer.playRandom()
                rest = np.random.choice([1,2,4,8],1,
                                        p=[0.15,0.7,0.1,0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()

    if args.piano:
        while True:
            for event in pygame.event.get():
                if(event.type==pygame.KEYUP):
                    print('key pressed')
                    nplayer.playRandom()
                    time.sleep(0.5)

if __name__=='__main__':
    main()