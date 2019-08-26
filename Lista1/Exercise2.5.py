#Exercise 2.
#Calcula a Transmissividade e Reflectividade de uma partícula ao encontrar um poço de potencial

from math import sqrt,pi

massa = float(input('Insira a massa da partícula (em kg)\n'))
energia = float(input('Insira a energia da partícula (em eV)\n'))
potencial = float(input('Insira o valor do potêncial (em eV)\n'))


c = 299792458 #(m/s)
h_cortado = 6.62607004*10**(-34) #(SI)

energia *= 1.60218*10**(-19) #conversão para SI
potencial *= 1.60218*10**(-19) #conversão para SI

DeltaE = energia-potencial

k_1 = sqrt((2*massa)*energia)/h_cortado
k_2 = sqrt(2*massa*(DeltaE))/h_cortado

T = 4*k_1*k_2/((k_1 + k_2)**2)
R = ((k_1 - k_2)**2)/((k_1 + k_2)**2)

print("Probabilidade de transmissão: ",T)
print("Probabilidade de reflexão: ",R)
