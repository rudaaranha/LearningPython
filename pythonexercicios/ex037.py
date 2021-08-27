#Ex037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 binário;
#-2 octal;
#-3 hexadecimal.
from time import sleep
print('Este é um programa que pode converter um número inteiro qualquer em binário, octal ou hexadecimal.')
num = int(input('Digite o número que você pretende converter:'))
print('''Para selecionar a base de conversão a ser realizada, escolha dentre as opções abaixo:
'[1] - Binário;
'[2] - Octal;
'[3] - Hexadecimal.''')
conv = str(input('Qual será a base de conversão (digite 1, 2 ou 3):'))
if conv == '1':
    sleep(1)
    nbin = bin(num)[2:]
    print('O número {} convertido para binário é {}.'.format(num, nbin))
elif conv == '2':
    sleep(1)
    noct = oct(num)[2:]
    print('O número {} convertido para octal é {}.'.format(num, noct))
elif conv == '3':
    sleep(1)
    nhex = hex(num)[2:]
    print('O número {} convertido para hexadecimal é {}.'.format(num, nhex))
else:
    sleep(1)
    print('\033[31mOpção inválida!\033[m')
print('Tenha um bom dia!')
