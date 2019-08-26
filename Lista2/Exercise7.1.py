from numpy import zeros,loadtxt
from pylab import plot,xlim,show,ylabel
from cmath import exp,pi
from math import sin

def dft(y):#calculates the dft (taken from newmans book)
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

#defining all 3 functions

y = zeros(1000)#square wave
v = zeros(1000)#sawtooth wave
w = zeros(1000)#modulated sine wave

for i in range(500):#square wave
    y[i] = 1
    y[i+500] = 0

for i in range(1000):# sawtooth wave
    v[i] = i
    
for i in range(1000):#modulated sine wave
    w[i] = (sin(i*pi/1000))*(sin(20*i*pi/1000))

#calculates their transform
    
c1 = dft(y)
c2 = dft(v)
c3 = dft(w)

#plots the transforms

plot(y)
ylabel("square-wave")
show()

plot(abs(c1))
ylabel("square-wave")
xlim(0,500)
show()

plot(v)
ylabel("sawtooth wave")
show()

plot(abs(c2))
ylabel("sawtooth wave")
xlim(0,500)
show()


plot(w)
ylabel("modulated sine wave")
show()

plot(abs(c3))
ylabel("modulated sine wave")
xlim(0,500)
show()
