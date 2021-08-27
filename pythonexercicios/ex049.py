#Ex049 - Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando o laço for.
#(Ex009)Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('Este programa mostra a tabuada de um número inteiro entre 0 e 10.')
n = int(input('Digite um número:'))
print('A tabuada do número {} é:'. format(n))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
