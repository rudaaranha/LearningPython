#Ex074 -  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número é {max(num)}.')
print(f'O menor número é {min(num)}.')
print('FIM.')