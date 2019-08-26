#Here i used Newton's Method

def f(r):
    
    G = 6.674*10**(-11)#m^3*/kg*s^2
    M = 5.974*10**24#kg
    m = 7.348*10**22#kg
    R = 3.844*10**8#m
    w = 2.662*10**(-6)#rad/s
    
    return G*M/(r**2) - G*m/((R - r)**2) - (w**2)*r

def df(r):
    
    G = 6.674*10**(-11)#m^3*/kg*s^2
    M = 5.974*10**24#kg
    m = 7.348*10**22#kg
    R = 3.844*10**8#m
    w = 2.662*10**(-6)#rad/s
    
    return -2*G*M/(r**3) - 2*G*m/((R - r)**3) - (w**2)

guess = 1
accuracy = 10**(-5)

x1 = guess
x2 = x1-f(x1)/df(x1)

while(abs(x2-x1)>accuracy):#the error for the newton method
                           #according to equation 6.101 from newmans book
    x1 = x2
    x2 = x1-f(x1)/df(x1)

print("The distance from the earth to the L1 point is",x2/1000,"kilometers")

