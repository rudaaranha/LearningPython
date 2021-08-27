#Ex016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor
print('Este é um programa que lê um número real qualquer e mostra sua porção inteira.')
n=float(input('Digite um número qualquer:'))
print('A porção inteira do número {} é igua a {}.'.format(n,floor(n)))
