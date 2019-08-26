A = int(input("enter A:\n"))
Z = int(input("enter Z:\n"))

if(A%2!=0):
    a_5 = 0
elif(A%2==0 and Z%2==0):
    a_5 = 12
elif(A%2==0 and Z%2!=0):
    a_5 = -12

B = 15.8*A - 18.3*A**(2/3) - (0.714*Z**2)/(A**(1/3)) - (23.2*(A - 2*Z)**2)/A + a_5/(A**(1/2))

print('The binding energy is ',B," MeV")# item (a)


print('The binding energy per nucleon is ',B/A," MeV") #item (b)


#A Partir daqui item (c)---------------------

Z = int(input("enter Z (corresponding to item c):\n"))

A=Z

if(A%2!=0):
    a_5 = 0
elif(A%2==0 and Z%2==0):
    a_5 = 12
elif(A%2==0 and Z%2!=0):
    a_5 = -12

aux = 15.67*A - 17.23*A**(2/3) - (0.75*Z**2)/(A**(1/3)) - (93.2*(A - 2*Z)**2)/A + a_5/(A**(1/2))
aux_A = A


for A in range(Z,3*Z+1):

    if(A%2!=0):
        a_5 = 0
    elif(A%2==0 and Z%2==0):
        a_5 = 12
    elif(A%2==0 and Z%2!=0):
        a_5 = -12
    
    B_max = 15.67*A - 17.23*A**(2/3) - (0.75*Z**2)/(A**(1/3)) - (93.2*(A - 2*Z)**2)/A + a_5/(A**(1/2))
    B_max = B_max/A
    
    if(B_max>aux):   
        aux = B_max
        aux_A = A
        
print('the value of A for the most stable nucleus is ',aux_A,'and its binding energy is ',aux)


#a partir daqui item (d)---------------------------------

check = input("type \"ready\" so it shows the results for item d)\n") #incluso para que o programa não tivesse um output enorme de uma vez

for Z in range(1,100):

    A=Z

    if(A%2!=0):
        a_5 = 0
    elif(A%2==0 and Z%2==0):
        a_5 = 12
    elif(A%2==0 and Z%2!=0):
        a_5 = -12

    aux = 15.67*A - 17.23*A**(2/3) - (0.75*Z**2)/(A**(1/3)) - (93.2*(A - 2*Z)**2)/A + a_5/(A**(1/2))
    aux_A = A


    for A in range(Z,3*Z+1):

        if(A%2!=0):
            a_5 = 0
        elif(A%2==0 and Z%2==0):
            a_5 = 12
        elif(A%2==0 and Z%2!=0):
            a_5 = -12
    
        B_max = 15.67*A - 17.23*A**(2/3) - (0.75*Z**2)/(A**(1/3)) - (93.2*(A - 2*Z)**2)/A + a_5/(A**(1/2))
        B_max = B_max/A
    
        if(B_max>aux):   
            aux = B_max
            aux_A = A
        
    print('the value of A for the most stable nucleus is ',aux_A,'and its binding energy per nucleon is ',aux, 'when Z is equal to ',Z)

