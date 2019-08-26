from numpy import loadtxt
import pylab as pl

#item (a)

data = loadtxt("sunspots.txt",float)# lê o txt
x = data[:,0]
y = data[:,1]
pl.plot(x,y)
pl.xlabel("Time")
pl.ylabel("Sunspots")
pl.show()

#item (b)

x = data[:1001,0]
y = data[:1001,1]
pl.plot(x,y)
pl.xlabel("Time")
pl.ylabel("Sunspots")
pl.show()

#item (c)

r = 5


ave = [0]*len(y)

for i in range(0,len(y)):
    ave[i] = y[i]

for k in range(r,len(y)-r):
    
    avesum = 0
    
    for m in range(k-r,k+r):
        avesum = avesum + y[m]
    
    ave[k] = (1/(2*r))*avesum
    
pl.plot(x,y)
pl.plot(x,ave,"r--")
pl.xlabel("Time")
pl.ylabel("Sunspots")
pl.show()
