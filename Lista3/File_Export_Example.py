from numpy import loadtxt,exp,zeros
from matplotlib.pyplot import show,plot,xlabel,ylabel

"""
#open the file in writing mode
f = open("export.txt", "w+")
#use the f.write function, it takes in only one argument and its basically printf from C but with % as separator
for i in range(100):
    f.write("%d   %f\n" % ((i),(exp(i))))
#close the file when done
f.close()
"""

data = loadtxt("exercise810b.txt",float)# lê o txt

t = data[:,0]
x = data[:,1]
y = data[:,2]
z = zeros(len(t))

plot(t,y,"b")
plot(t,x,"r")
xlabel("t")
ylabel("y in blue, x in red ")
show()

plot(x,y)
xlabel("x")
ylabel("y")
show()

