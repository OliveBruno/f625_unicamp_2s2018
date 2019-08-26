from random import random
from numpy import arange
from matplotlib.pyplot import plot,xlabel,ylabel,show,title,legend

#Constants
BI2131 = 10000             #initial value of 213 Bi
Tl2091 = 0                 #initial value of 209 Tl
Pb2091 = 0                 #initial value of 209 Pb
BI2091 = 0                 #initial value of 209 Bi
tau213BI = 46*60          #Half life of 213 Bi in seconds
tau209Tl = 2.2*60         #Half life of 209 Tl in seconds
tau209Pb = 3.3*60         #Half life of 209 Pb in seconds
h = 1                       #Size of time-step in seconds
P213BI = 1 - 2**(-h/tau213BI) #Probability of decay of 213 Bi in one step
P209Tl = 1 - 2**(-h/tau209Tl) #Probability of decay of 209 Tl in one step
P209Pb = 1 - 2**(-h/tau209Pb) #Probability of decay of 209 Pb in one step
tmax = 20000                #Total time

#Lists of plot points
tpoints = arange(0,tmax,h)
BI213points = []
Tl209points = []
Pb209points = []
BI209points = []

# Main loop
for t in tpoints:
    BI213points.append(BI2131)
    Tl209points.append(Tl2091)
    Pb209points.append(Pb2091)
    BI209points.append(BI2091)    

    # Calculate the number of atoms that decay
    decayBItoTl = 0
    decayTltoPb = 0
    decayBItoPb = 0
    decayPbto209BI = 0    

    
    for i in range(BI2131):
        
        a = random()

        if(a < P213BI and a < (2.09/100)*P213BI):
            decayBItoTl += 1
        elif(a < P213BI and a > (2.09/100)*P213BI):
            decayBItoPb += 1

    for i in range(Tl2091):
        if(random()<P209Tl):
            decayTltoPb += 1

    for i in range(Pb2091):
        if(random()<P209Pb):
            decayPbto209BI += 1

    BI2131 -= (decayBItoTl + decayBItoPb)
    Tl2091 += (decayBItoTl - decayTltoPb)
    Pb2091 += (decayBItoPb + decayTltoPb - decayPbto209BI)
    BI2091 += (decayPbto209BI) 
    
    
#Make the graph
plot(tpoints,BI213points,"b",label = "213Bi")
plot(tpoints,Tl209points,"g",label = "209Tl")
plot(tpoints,Pb209points,"r",label = "209Pb")
plot(tpoints,BI209points,"m",label = "209Bi")
xlabel("Time (seconds)")
ylabel("Number of atoms")
legend()
show()
