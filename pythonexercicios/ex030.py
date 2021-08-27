#Ex030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
from time import sleep
print('Este programa lê um número inteiro e diz se ele é par ou impar.')
num = int(input('Digite um número:'))
resultado = num % 2
print('Analisando o número...')
sleep(2)
if resultado == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
