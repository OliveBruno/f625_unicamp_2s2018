from numpy import array,arange
from pylab import plot,xlabel,ylabel,show

def f(r,t):
    
    x = r[0]
    y = r[1]
    z = r[2]
    fx = 10*(y - x)
    fy = 28*x - y - x*z
    fz = x*y - (8/3)*z
    
    return array([fx,fy,fz],float)

a = 0.0#initial value for t
b = 50.0#final value for t
N = 10000#number of slices
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0,1.0,0.0],float)#initial condiditons are added here

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
    
plot(tpoints,ypoints)
ylabel("y")
xlabel("t")
show()

plot(xpoints,zpoints)
xlabel("x")
ylabel("z")
show()
