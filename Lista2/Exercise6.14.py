from math import tan,sqrt
from scipy import constants as cte
from numpy import zeros
import pylab as pl

def y1(E):# it was a pain inserting all the constants every time
    #so i reduced the number of variables to just the energy in eV

    w = 10**(-9)# from problem 6.14
    m = 9.1094*10**(-31)# electron mass    
    arg = ((w**2)*m/((2*(cte.hbar**2))))*(cte.e)#i chose to deal with all of the constants here
                                                #instead of inside the tan(sqrt())  
    
    return tan(sqrt(arg*E))

def y2(E):
    V = 20#eV
    return sqrt((V-E)/E)

def y3(E):
    V = 20#eV
    return -sqrt(E/(V-E))

def diffy12(E):
    w = 10**(-9)# from problem 6.14
    m = 9.1094*10**(-31)# electron mass
    V = 20#eV
    arg = ((w**2)*m/((2*(cte.hbar**2))))*(cte.e)    
    
    return tan(sqrt(arg*E))-sqrt((V-E)/E)

def diffy13(E):
    w = 10**(-9)# from problem 6.14
    m = 9.1094*10**(-31)# electron mass
    V = 20#eV
    arg = ((w**2)*m/((2*(cte.hbar**2))))*(cte.e)    
    
    return tan(sqrt(arg*E))+sqrt(E/(V-E))

def Binary_Searchy2(a,b,accuracy):# i made 2 binary searches, one for each function...
    #i was having too much trouble trying to create a function for a general case so i dropped it
    
    while(abs(b-a) > accuracy ):
        
        if(diffy12(0.5*(a+b))*diffy12(a) > 0):
            a = 0.5*(a+b)
        else:
            b = 0.5*(a+b)

    return 0.5*(a+b)

def Binary_Searchy3(a,b,accuracy): 
    
    while(abs(b-a) > accuracy ):
        
        if(diffy13(0.5*(a+b))*diffy13(a) > 0):
            a = 0.5*(a+b)
        else:
            b = 0.5*(a+b)

    return 0.5*(a+b)

x = zeros(1000)
y_1 = zeros(1000)
y_2 = zeros(1000)
y_3 = zeros(1000)


for i in range(1,1000):
    x[i] = i*20/1000
    y_1[i] = y1(x[i]) 
    y_2[i] = y2(x[i])
    y_3[i] = y3(x[i])

E0 = Binary_Searchy3(1,1.5,10**(-3))
E1 = Binary_Searchy2(1,3,10**(-3))
E2 = Binary_Searchy3(4.5,5.5,10**(-3))
E3 = Binary_Searchy2(7.5,8.5,10**(-3))
E4 = Binary_Searchy3(10.5,11.5,10**(-3))
E5 = Binary_Searchy2(14.5,15.5,10**(-3))


print("the first energy level is",E0,"eV")
print("the second energy level is",E1,"eV")
print("the third energy level is",E2,"eV")
print("the fourth energy level is",E3,"eV")
print("the fifth energy level is",E4,"eV")
print("the sixth energy level is",E5,"eV")

pl.plot(x,y_1,"r.")
pl.ylim([-3.5,3.5])
pl.plot(x,y_2,"b.")
pl.ylim([-3.5,3.5])
pl.plot(x,y_3,"g.")
pl.ylim([-3.5,3.5])
pl.xlabel("Energies")
pl.ylabel("y1 is red, y2 is blue and y3 is green")
pl.show()
