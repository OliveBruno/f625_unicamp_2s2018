from numpy import loadtxt
import pylab as pl
from numpy import zeros

data = loadtxt("velocities.txt",float)

t = data[:,0]#time
v = data[:,1]#velocities in the x axis at time t
m = len(t)


x = zeros(m)

for i in range(0,len(t)):
    
    a = int(t[0])
    b = int(t[i])
    if(b == 0):
        h = 1
    else:
        h = (b-a)/b
    
    s = 0
    
    s = 0.5*v[a] + 0.5*v[b]
    
    if(i>1 or i ==1):
        for k in range(1,b):            
            aux = int(a + k*h)
            s += v[aux]
    
    x[i] = s*h
    
pl.plot(t,v,"ro")
pl.plot(t,x,"bo")
pl.xlabel("Time")
pl.ylabel("Position (blue) and Velocity (red)")
pl.show()
