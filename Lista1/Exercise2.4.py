#Exercicio 2.4

import math

x = float(input('Entre com a distância em anos-luz:\n'))#x é distancia até outro planeta x anos luz de distância
v = float(input('Entre com a velocidade da espaçonave (como fração da velocidade da luz \'c\'):\n'))

print('no referencial da Terra, o tempo de chegada é:  ',x/v ,'anos')
print('no referencial do passageiro na espaçonave, o tempo de chegada é:  ',x/(v*(1/(math.sqrt(1 - v**2)))) ,'anos')
