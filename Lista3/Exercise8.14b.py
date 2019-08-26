from numpy import array,arange,zeros
from matplotlib.pyplot import show,plot,xlabel,ylabel,legend
from math import sqrt
from time import time

#constants
m = 9.1094e-31      #electron mass
hbar = 1.0546e-34   #planck constant divided by 2pi
e = 1.6022e-19      #electron charge
N = 1000
a = 10**(-11)
h = a/N
rangestart = -5*a
rangeend = -rangestart

#potential function
V0 = 50*e#eV
def V(x):
    return V0*((x/a)**4)

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# calculate the wavefunction for a particular energy
def solve(E):
    psi = 0
    phi = 1
    r = array([psi,phi],float)

    xpoints = arange(rangestart,rangeend,h)
    psipoints = []

    for x in xpoints:
        psipoints.append(r[0])
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return r[0],psipoints

def Normalize(vect,end):#calculates the integral using the trapezoidal rule
                        #from the start to the given end
    
    a = int(0) #initial point
    b = int(end) #end point
    
    s = 0.5*(vect[a]**2) + 0.5*(vect[b]**2)
    for k in range(1,b):
        aux = int(a+k*h)
        s += (vect[aux])**2

    return sqrt(h*s)
    


# Main program to find the energies using the secant method


aux = 0
target = e/100000

#fundamental state

fundpoints = []

E1 = 100*e
E2 = 200*e
psi2,fundpoints = solve(E1)

while(abs(E1-E2)>target):
    psi1 = psi2
    psi2,fundpoints = solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

aux,fundpoints = solve(E2)


print("The energy of the fundamental state is E0 =",E2/e,"eV")


#first excited state
ex1points = []

E1 = 400*e
E2 = 500*e
psi2,ex1points = solve(E1)

while(abs(E1-E2)>target):
    psi1 = psi2
    psi2,ex1points = solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

aux,ex1points = solve(E2)


print("The energy of the first excited state is E1 =",E2/e,"eV")


#second excited state
ex2points = []

E1 = 1400*e
E2 = 1500*e
psi2,ex1points = solve(E1)

while(abs(E1-E2)>target):
    psi1 = psi2
    psi2,ex2points = solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

aux,ex2points = solve(E2)


print("The energy of the second excited state is E2 =",E2/e,"eV")

xpoints = arange(rangestart,rangeend,h)


normfund = (2*Normalize(fundpoints,len(fundpoints)/2))
norm1 = (2*Normalize(ex1points,len(ex1points)/2))
norm2 = (2*Normalize(ex2points,len(ex2points)/2))


for i in range(len(fundpoints)):    
    fundpoints[i] /= normfund

for i in range(len(ex1points)): 
    ex1points[i] /= norm1
    
for i in range(len(ex2points)): 
    ex2points[i] /= norm2


plot(xpoints,fundpoints,"b",label="Fundamental state")
plot(xpoints,ex1points,"r",label="First excited state")
plot(xpoints,ex2points,"g",label="Second excited state")
legend()
show()
