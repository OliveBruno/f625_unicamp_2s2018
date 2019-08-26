import pylab as pl
from math import sqrt
from numpy import zeros,arange
from numpy import ones,copy,cos,tan,pi,linspace

#THIS FUNCTION WAS TAKEN FROM NEWMAN'S WEBSITE

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w


def f(a,x):
    return sqrt(8/(a**4 - x**4))

#THIS FUNCTION WAS ADAPTED FROM EXAMPLE 5.2

def GaussIntegral(b):#calculates an integral using gaussian quadrature by taking the upper limit as an input

#the lower limit is "a" and it is set to 0.0 by default
    
    N = 20
    a = 0.0

    #Calculate the sample points and weights, then map them
    #to the required integration domain

    x,w = gaussxw(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w

    #Perform the integration
    s = 0.0
    for k in range(N):
        s += wp[k]*f(b,xp[k])

    return s


x = arange(0,2,0.02)
y = []
v = 0.0

for i in x:
    y.append(v)
    v = GaussIntegral(x[i])

pl.plot(x,y,"o")
pl.xlabel("Amplitude")
pl.ylabel("Period")
pl.show()
