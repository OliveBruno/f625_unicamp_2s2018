from random import randrange

counter = 0

for i in range(10**6):
    a = randrange(1,7)
    b = randrange(1,7)
    if(a == 6 and b == 6):
        counter += 1

print("The fraction of times a double 6 happened was",counter/(10**6))
print("The expected fraction was", 1/36)
