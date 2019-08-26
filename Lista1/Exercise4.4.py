from math import sqrt,pi
from time import time


def Integral(N):

    h = 2/N

    sum = 0
    for k in range(1,N+1):
        sum = sum + h*(sqrt(1 - (-1+h*k)**2))
    
    return sum

#item a)

I100 = Integral(100)

print("The value of the integral for N = 100 is ",I100)
print("The analitical value of the integral is ",pi/2)

#item b)

t0=time()
I1sec=Integral((10**6)+(5*10**5))
t1=time()

print("The value of the integral after ~1 sec runtime is ",I1sec)
print("Tempo de execução ",t1-t0,"segundos")

"""
usando um valor de N = 1.5e6 foi possível obter o valor com uma precisão de 9 casas decimais em aproximadamente 1 segundo

"""
