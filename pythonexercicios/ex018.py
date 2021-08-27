#Ex018 - Faça um programa que leia um ângulo qualquer e mostre o valor do seno, do cosseno e da tangente do mesmo
from math import radians, sin, cos, tan
print('Este programa lê um ângulo qualquer e calcula seu seno, cosseno e tangente.')
a=float(input('Digite um ângulo qualquer:'))
sen=sin(radians(a))
cos=cos(radians(a))
tan=tan(radians(a))
print('Os valores do seno, cosseno e tangente para o ângulo {}, são iguais a {:.2f}, {:.2f} e {:.2f}, respectivamente.'.format(a,sen,cos,tan))
