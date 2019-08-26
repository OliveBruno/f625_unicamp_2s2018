from math import exp
from numpy import zeros
import pylab as pl

def f(c,x):#f(x)
    return 1-exp(-c*x)

def df(c,x):#f'(x)
    return c*exp(-c*x)

def error1(x,x1,x2,c):#formula 6.84 from newman's book
    return (x1-x2)/(1 - 1/df(c,x))

def relaxation_method(guess,c):#takes in a "guess" value and the parameter of the function f(x) as input

    x = f(c,guess)
    x1 = f(c,x)
    x2 = f(c,x1)

    while (abs(error1(x,x1,x2,c)) > 10**(-6)):
        x = x1
        x1 = x2
        x2 = f(c,x2)

    return f(c,x2)

print(relaxation_method(1,2))#item a)

x = zeros(301)
c = zeros(301)

for i in range(1,300):
    c[i] = i*0.01
    x[i] = relaxation_method(1,c[i])

pl.plot(c,x,".")
pl.xlabel("c")
pl.ylabel("x")
pl.show()
