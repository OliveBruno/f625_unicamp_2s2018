from numpy import array,arange
from pylab import plot,xlabel,ylabel,show
from math import sqrt
from scipy.constants import G

def f(r,t):
    
    M = 1.989*(10**30)#in kg
    
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    Dvx = (-G*M*x)/((x**2 + y**2)**(3/2))
    Dvy = (-G*M*y)/((x**2 + y**2)**(3/2))
    
    return array([vx,vy,Dvx,Dvy],float)

def Verlet(r,tpoints,h):#takes in initial conditions, the time range and the step

    xpoints = []
    ypoints = []
    vxpoints = []
    vypoints = []

    
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        vxpoints.append(r[2])
        vypoints.append(r[3])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    return xpoints,ypoints,tpoints

a = 0#initial value for t
b = 10**10#final value for t
h = 3600 #seconds or 1 hour
#N = 10**6#number of slices
#h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([-1.4710*10**11,0,0,3.0287*10**4],float)#initial condiditons are added here


xpoints,ypoints,tpoints = Verlet(r,tpoints,h)


plot(xpoints,ypoints,"b.")
ylabel("y")
xlabel("x")
show()
