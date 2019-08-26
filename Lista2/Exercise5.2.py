def f(x):
    return x**4 - 2*x + 1

def SRule(y):
    
    N = y# number of slices
    a = 0.0# lower limit
    b = 2.0# upper limit

    h = (b-a)/N# size of the slice

    s = f(a) + f(b)

    for k in range(1,N,2):
        s += 4*f(a+k*h)
    
    for k in range(2,N,2):
        s += 2*f(a+k*h)
    

    print("The value of the integral is",(1/3)*h*s,"for",N,"slices")
    print("The fractional error is",(((1/3)*h*s)/4.4 - 1))

    return 0

SRule(10)
SRule(100)
SRule(1000)
