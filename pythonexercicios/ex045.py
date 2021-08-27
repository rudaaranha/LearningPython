#Ex045 - Crei um programa que faça o computador jogar jokenpô com você.
from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA') #possíveis escolha do jogo... pedra, papel e tesoura
comp = randint(0, 2) #escolha random do computador
print('{:=^40}'.format(' JO KEN PO ')) #O código '{:-^40}' faz com que a palavra jo ken po apareça com uma distância de 40 caracteres.
print('Vamos jogar JO KEN PO!')
sleep(0.5)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('Qual a sua jogada?'))
print('-='*25)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-='*25)
print('O computador escolheu {}.'.format(itens[comp]))
print('Você escolheu {}.'.format(itens[escolha]))
print('-='*25)
if comp == 0 and escolha == 0 or comp == 1 and escolha == 1 or comp == 2 and escolha == 2:
    print('As escolhas foram iguais. Vocês EMPATARAM.')
elif comp == 0 and escolha == 2 or comp == 1 and escolha == 0 or comp == 2 and escolha == 1:
    print('O computador VENCEU!')
elif comp == 0 and escolha == 1 or comp == 1 and escolha == 2 or comp == 2 and escolha == 0:
    print('O jogador VENCEU!')
else:
    print('Escolha inválida, tente novamente.')
