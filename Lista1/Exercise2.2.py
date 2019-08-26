#Exercícios da lista de F625

from math import pi

#Exercício 2.2

T = float(input("Digite o período (somente o número)\n"))

G = 6.67*10**-11
M = 5.97*10**24
R = 6371*10**3

unit = input("insira a unidade (ie, segundos, minutos, horas...)\n")

if(unit == 'segundo' or unit == 'segundos'):
    T = T
    h = ((G * M * T ** 2) / (4 * pi ** 2)) ** (1 / 3) - R
elif(unit == 'minuto' or unit == 'minutos'):
    T *= 60
    h = ((G * M * T ** 2) / (4 * pi ** 2)) ** (1 / 3) - R
elif(unit == 'horas' or unit == 'hora'):
    T *= 3600
    h = ((G * M * T ** 2) / (4 * pi ** 2)) ** (1 / 3) - R
elif(unit == 'dias' or unit == 'dia'):
    T *= 3600*24
    h = ((G * M * T ** 2) / (4 * pi ** 2)) ** (1 / 3) - R
elif(unit == 'anos' or unit == 'ano'):
    T *= 3600*24*365
    h = ((G * M * T ** 2) / (4 * pi ** 2)) ** (1 / 3) - R
else:
    print('unidade não suportada: ',unit)
    h = 0

print("A altitude da órbita é",h,"metros!")
