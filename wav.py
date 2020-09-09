import numpy as np
import wave,math

sRate = 44100 #采样率
nSamples = sRate *5


x= np.arange(nSamples)/float(sRate)
y=np.arange(nSamples)
vals = np.sin(2.0*math.pi*220.0*x)  #创建振幅值的numpy数组

data = np.array(vals*32767,'int16').tostring()

file = wave.open('sine220.wav','wb')
file.setparams((1,2,sRate,nSamples,'NONE','uncompressed'))
file.writeframes(data)
file.close()