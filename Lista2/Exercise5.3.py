from math import exp,erf,pi,sqrt
from numpy import empty
import pylab as pl

def f(t):
    return exp(-(t**2))

def E_SR(x):
    

    N = 1000# number of slices
    a = 0.0# lower limit
    b = x# upper limit

    if(b==a):
        return 0
    
    h = (b-a)/N# size of the slice

    s = f(a) + f(b)

    for k in range(1,N,2):
        s += 4*f(a+k*h)
    
    for k in range(2,N,2):
        s += 2*f(a+k*h)
    
    expected = (sqrt(pi)/2)*erf(x)
    
    #print(expected)
    
    return (1/3)*h*s


y1 = empty(2000)
x = empty(2000)

for k in range(-1000,1000):
    y1[k] = E_SR(k/200)
    x[k] = k/200

pl.plot(x,y1,"ro")
pl.xlabel("x")
pl.ylabel("E(x)")
pl.show()

