from numpy import loadtxt
import pylab as pl
from decimal import Decimal

#item a)

data = loadtxt("millikan.txt",float)# lê o txt

x = data[:,0] #isto será a frequência em hertz
y = data[:,1] #isto será a voltagem em volts
pl.plot(x,y,"o")
pl.xlabel("x")
pl.ylabel("y")
pl.show()

#item b)

sumx = 0
sumy = 0
sumxx = 0
sumxy = 0

for i in range(0,len(x)):
    sumx=x[i]+sumx
    sumy=y[i]+sumy
    sumxx=x[i]*x[i]+sumxx
    sumxy=x[i]*y[i]+sumxy

Ex = (1/len(x))*sumx
Ey = (1/len(x))*sumy
Exx = (1/len(x))*sumxx
Exy = (1/len(x))*sumxy

m = (Exy - Ex*Ey)/(Exx-Ex*Ex)
c = (Exx*Ey-Ex*Exy)/(Exx-Ex*Ex)

print("The slope \"m\" of the best- fit line is",'%.2E' % Decimal(m),"and its intercept \"c\" is",'%.2E' % Decimal(c))

#item c)

v = [0]*len(x)

for i in range(0,len(x)):
    v[i]=m*x[i]+c

pl.plot(x,y,"o")
pl.plot(x,v,'r--')
pl.xlabel("x")
pl.ylabel("y")
pl.show()

#item d)

e = 1.602*10**-19 #carga do eletron em Coulomb

h = m*e #segue da equação dada

print(" The value of Planck's constant is then h =",'%.2E' % Decimal(h),"Js")
