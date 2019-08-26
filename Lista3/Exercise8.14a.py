from numpy import array,arange
from matplotlib.pyplot import show,plot,xlabel,ylabel

#constants
m = 9.1094e-31      #electron mass
hbar = 1.0546e-34   #planck constant divided by 2pi
e = 1.6022e-19      #electron charge
N = 1000
a = 10**(-11)
h = a/N

V0 = 50*e#eV

#potential function
def V(x):
    return V0*((x/a)**2)

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

    for x in arange(-10*a,10*a,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return r[0]

# Main program to find the energies using the secant method

#fundamental state
E1 = 100*e
E2 = 200*e
psi2 = solve(E1)

target = e/100000
while(abs(E1-E2)>target):
    psi1,psi2 = psi2,solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

print("The energy of the fundamental state is E0 =",E2/e,"eV")

#first excited state

E1 = 400*e
E2 = 500*e
psi2 = solve(E1)

while(abs(E1-E2)>target):
    psi1,psi2 = psi2,solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

print("The energy of the first excited state is E1 =",E2/e,"eV")

#second excited state

E1 = 600*e
E2 = 700*e
psi2 = solve(E1)

while(abs(E1-E2)>target):
    psi1,psi2 = psi2,solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

print("The energy of the second excited state is E2 =",E2/e,"eV")







