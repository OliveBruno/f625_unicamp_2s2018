from numpy import array,arange
from pylab import plot,xlabel,ylabel,show
from math import sqrt
from scipy.constants import G
from time import time

def f(r,t):
    
    M = 1.989*(10**30)#in kg    
    
    x = r[0]
    y = r[1]
    Dx = r[2]#vx
    Dy = r[3]#vy
    
    DDx = (-G*M*x)/((x**2 + y**2)**(3/2))
    DDy = (-G*M*y)/((x**2 + y**2)**(3/2))
    
    return array([Dx,Dy,DDx,DDy],float)

def RungeKutta(r,tpoints,h):#takes in initial conditions, the time range and the step

    xpoints = []
    ypoints = []
    Dxpoints = []
    Dypoints = [] 

    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        Dxpoints.append(r[2])
        Dypoints.append(r[3])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    return xpoints,ypoints,tpoints

a = 0#initial value for t
b = 10**10#final value for t
N = 10**6#number of slices
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([4*(10**12),0,0,500],float)#initial condiditons are added here

a1 = time()

xpoints,ypoints,tpoints = RungeKutta(r,tpoints,h)

a2 = time()
print("The stepsize (h) is equal to",h)
print("Calculation lasted",a2-a1,"seconds")

plot(xpoints,ypoints,"b.")
ylabel("y")
xlabel("x")
show()
