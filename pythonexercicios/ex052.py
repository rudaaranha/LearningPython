#Ex052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número:'))
cont = 0
for c in range(1, num + 1): #tem que ter o num+1 porque o python sempre conta um número a menos dentro do for.
    if num % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('O número {} é um número primo!'.format(num))
else:
    print('O número {} não é um número primo!'.format(num))
