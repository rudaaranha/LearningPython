#Ex068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-='*14)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*14)
vitorias = 0
while True:
    n = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0] #O zero entre colchetes significa que só vai pegar a primeira letra
    computador = randint(0, 10) #comando que faz o computador escolher um número aleatório entre 0 e 10.
    s = n + computador
    resultado = s % 2
    print('-'*28)
    if resultado == 0:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {s} DEU PAR.')
        print('-'*28)
        if pi == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias = vitorias + 1 #contagem do número de vitórias
            print('-=' * 14)
        else:
            break
    else:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {s} DEU ÍMPAR.')
        print('-'*28)
        if pi == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias = vitorias + 1 #contagem do número de vitórias
            print('-='*14)
        else:
            break
print('Você PERDEU!')
print('-='*14)
print(f'GAME OVER! Você venceu {vitorias} vez(es).')
