from vpython import sphere,vector,color,display,rate
from numpy import empty,arange
from math import cos,sin,pi

#d = display(background=color.white)

s = empty(7,sphere)

R = [695500,2440,6052,6371,3386,69173,57316]
Dist = [0,57.9,108.2,149.6,227.9,778.5,1433.4]
T = [0,88,224.7,365.3,687,4331.6,10759.2]

i=0

s[i]=sphere(pos=vector(Dist[i]*10**6,0,0),radius = 50*R[i])

for i in range(6):
    s[i+1]=sphere(pos=vector(Dist[i+1]*10**6,0,0),radius = 250*R[i+1])

s[0].color = color.yellow
s[1].color = vector(165,113,78)/255
s[2].color = color.orange
s[3].color = color.blue
s[4].color = color.red
s[5].color = vector(250,218,94)/255
s[6].color = vector(213,196,161)/255

for theta in arange(0,1000*pi,(1/100)*pi):
    rate(100)
    for i in range(6):
        x = Dist[i+1]*cos(2*theta/T[i+1])*10**6
        z = Dist[i+1]*sin(2*theta/T[i+1])*10**6
        s[i+1].pos = vector(x,0,z)
