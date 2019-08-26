import numpy as np
from pylab import show,xlabel,ylabel,plot,legend

y = np.loadtxt("dow.txt",float)#item a)

plot(y,"b")
xlabel("Day")
ylabel("Daily closing value")
show()

c = np.fft.rfft(y)#item b)

for i in range(int(len(c)/10),len(c)):#item c)
    c[i] = 0

smooth = np.fft.irfft(c)#item d)

plot(y,"b",label= "Original data")
plot(smooth,"g",label = "Smooth data")
xlabel("Day")
#ylabel("Original data in blue and smoother data in red")
legend(loc = 1)
show()

c = np.fft.rfft(y)#item e)

for i in range(int(len(c)/50)):
    c[i] = 0

noise = np.fft.irfft(c)

plot(y,"b",label = "Original data")
plot(smooth,"g",label = "Smooth data")
plot(noise,"r",label = "Noise")
xlabel("Day")
#ylabel("Original data in blue and noise data in red")
legend(loc = 1)
show()
