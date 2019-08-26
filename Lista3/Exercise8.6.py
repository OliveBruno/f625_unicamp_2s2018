from numpy import array,arange
from pylab import plot,xlabel,ylabel,show,legend

def functiona(r,t,*args):#function asked in items a and b,  it takes in r, t and a frequency, in this order
    
    if (args != ()):#sets the frequency to 1 if none is given
        w = args[0]
    else:
        w = 1
    
    x = r[0]
    y = r[1]
    fx = y
    fy = -(w*w)*x
    
    return array([fx,fy],float)

def functionc(r,t,*args):#function asked in item c, it takes in r, t and a frequency, in this order
    
    if (args != ()):#sets the frequency to 1 if none is given
        w = args[0]
    else:
        w = 1
    
    x = r[0]
    y = r[1]
    fx = y
    fy = -(w*w)*x**3
    
    return array([fx,fy],float)

def functione(r,t,*args):#function asked in item e, it takes in r, t, a value of mu and a frequency, in this order
    
    if (len(args) >= 0):#sets mu to 1 if none is given
        mu = args[0]
    else:
        mu = 1
        
    if (len(args) >= 2):#sets the frequency to 1 if none is given
        w = args[1]
    else:
        w = 1
    
    x = r[0]
    y = r[1]
    fx = y
    fy = -(w*w)*x**3 + mu*(1 - x**2)*y
    
    return array([fx,fy],float)

def SolveEquation(r0,f):#solves and plots a given equation based on the initial conditions, plots the x coordinate vs t coordinate

    a = 0.0#initial value for t
    b = 50.0#final value for t
    N = 10000#number of slices
    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = []
    ypoints = []   

    for t in tpoints:
        xpoints.append(r0[0])
        ypoints.append(r0[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r0 += (k1+2*k2+2*k3+k4)/6
    
    return xpoints,ypoints

def SolveEquatione(r0,f,mu):#adjusted SolveEquation that works better to do item e, too lazy to do this better...

    a = 0.0#initial value for t
    b = 20.0#final value for t
    N = 50000#number of slices
    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = []
    ypoints = []   

    for t in tpoints:
        xpoints.append(r0[0])
        ypoints.append(r0[1])
        k1 = h*f(r,t,mu)
        k2 = h*f(r+0.5*k1,t+0.5*h,mu)
        k3 = h*f(r+0.5*k2,t+0.5*h,mu)
        k4 = h*f(r+k3,t+h,mu)
        r0 += (k1+2*k2+2*k3+k4)/6

    return xpoints,ypoints


#main program starts here------------



a = 0.0#initial value for t
b = 50.0#final value for t
N = 10000#number of slices
h = (b-a)/N


tpoints = arange(a,b,h)
y1points = []

r = array([1.0,0.0],float)
x1points = []
x1points,y1points = SolveEquation(r,functiona)


plot(tpoints,x1points,"b")
ylabel("Position")
xlabel("Time")
show()#item a)


r = array([2.0,0.0],float)
x2points = []
x2points,y1points = SolveEquation(r,functiona)

plot(tpoints,x1points,"b",label = "x(0) = 1")
plot(tpoints,x2points,"r",label = "x(0) = 2")
ylabel("Position")
xlabel("Time")
legend()
show()#item b)


r = array([1.0,0.0],float)

x1points,y1points = SolveEquation(r,functionc)
    
r = array([2.0,0.0],float)

x2points,y1points = SolveEquation(r,functionc)

plot(tpoints,x1points,"b",label = "x(0) = 1")
plot(tpoints,x2points,"r",label = "x(0) = 2")
ylabel("Position")
xlabel("Time")
legend()
show()#item c)

plot(x2points,y1points)
ylabel("Velocity")
xlabel("Position")
show()#item d)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

x1,y1 = SolveEquatione(r,functione,1)
x2,y2 = SolveEquatione(r,functione,2)
x3,y3 = SolveEquatione(r,functione,4)

plot(x1,y1,"r",label="mu = 1")
plot(x2,y2,"b",label="mu = 2")
plot(x3,y3,"g",label="mu = 4")
ylabel("Velocity")
xlabel("Position")
legend()
show()#item e)

