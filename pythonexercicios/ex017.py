#Ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa


#Utilizando "from math import sqrt"
from math import sqrt
print('Este programa lê o comprimento dos catetos de um triângulo retângulo qualquer e calcula sua hipotenusa.')
co=float(input('Qual o comprimento em milímetros do cateto oposto do triângulo?'))
ca=float(input('E do cateto adjacente?'))
hip=sqrt((co**2)+(ca**2))
print('O triâgulo cujo cateto oposte é {}mm e o cateto adjacente é {}mm, possui hipotenusa igual a {:.2f}mm'.format(co,ca,hip))

print('-'*130)

#Utilizando "import math"
import math
co2=float(input('Qual o comprimento em milímetros do cateto oposto do triângulo?'))
ca2=float(input('e do cateto adjacente?'))
hip2=math.sqrt((co2**2)+(ca2**2))
print('O triâgulo cujo cateto oposte é {}mm e o cateto adjacente é {}mm, possui hipotenusa igual a {:.2f}mm'.format(co2,ca2,hip2))