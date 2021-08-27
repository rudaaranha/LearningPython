#Ex088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
#serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
cont = 0
jogos = []
print('-'*40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('-'*40)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-= SORTEANDO {num} JOGOS -=-=-=-=-=')
while cont < num:
    for c in range(0, 6):
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
        else:
            n = randint(1, 60)
            jogos.append(n)
    jogos.sort()
    sleep(1)
    print(f'Jogo {cont + 1}: {jogos}')
    jogos.clear()
    cont = cont + 1
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

#Resolução do professor:
#from random import randint
#from time import sleep
#jogos = []
#lista = []
#print('-'*30)
#print('    JOGO DA MEGA SENA    ')
#print('-'*30)
#quant = int(input('Quantos jogos você quer que eu sorteie? '))
#tot = 1
#while tot <= quant:
#   cont = 0
#   while True:
#       num = randint(1, 60)
#       if num not in lista:
#           lista.append(num)
#           cont += 1
#       if cont >= 6:
#           break
#   lista.sort()
#   jogos.append(lista[:])
#   lista.clear()
#   tot += 1
#print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
#for i, l in enumerate(jogos):
#    print(f'Jogo {i+1}: {l}')
#    sleep(1)
#print('-='*5, f'< BOA SORTE! >', '-='*5)
