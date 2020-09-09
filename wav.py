import numpy as np
import wave,math

sRate = 44100 #采样率
nSamples = sRate *5


x= np.arange(nSamples)/float(sRate)

vals = np.sin(2.0*math.pi*220.0*x)  #根据正弦波方程创建振幅值的数组，创建振幅值的numpy数组A振幅=sin(2πfi/R)


data = np.array(vals*32767,'int16').tostring() #正玄波被放大为16位值，并转换为字符串，以便写入文件

file = wave.open('sine220.wav','wb')
file.setparams((1,2,sRate,nSamples,'NONE','uncompressed'))
file.writeframes(data)
file.close()