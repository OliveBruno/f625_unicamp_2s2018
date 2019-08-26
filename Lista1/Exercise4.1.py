def mod(x):

    if(x<0):
        x*=-1
    return x

def fact(n):
    
    if(n==0):
        return 1
    else:
        fact = n
    
        for i in range(1,int(n)):
            fact = fact*(n-i)
        return fact

#item a)

a = mod(int(input("insert an integer \"n\" \n")))
        
print("n! is equal to",fact(a))

#item b)

b = mod(float(input("insert a real number \"n\" \n")))
        
print("n! is equal to",fact(b))
