from numpy import zeros,loadtxt
from pylab import plot,xlim,show,xlabel,ylabel
from cmath import exp,pi
from time import time

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

data = loadtxt("sunspots.txt",float)# reads the txt file

x = data[:,0]
y = data[:,1]

#plots it

plot(x,y)
xlabel("Months")
ylabel("Sunspots")
show()

#calculates the dft

#for some reason it takes pretty long (~ 23 secs) to run this

t1 = time()

c = dft(y)

t2 = time()

print("tempo de execução =",t2-t1,"segundos")


#plots that dft

plot((abs(c))**2)
xlabel("k")
ylabel("Squared magnitude of the fourier coeficient")
xlim(0,1572)
show()

