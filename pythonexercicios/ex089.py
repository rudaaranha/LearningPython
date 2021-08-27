#Ex089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
#aluno individualmente.
from time import sleep
boletim = list()
nomesnotas = list()
while True:
    nomesnotas.append(str(input('Nome: ')))
    nomesnotas.append(float(input('Nota 1: ')))
    nomesnotas.append(float(input('Nota 2: ')))
    nomesnotas.append((nomesnotas[1] + nomesnotas[2])/2)
    boletim.append(nomesnotas[:])
    nomesnotas.clear()
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<16}{"MÉDIA":>8}')
print('-'*30)
for i, p in enumerate(boletim):
    print(f'{i:<3}',  f'{p[0]:<14}',  f'{p[3]:>8.2f}')
print('-'*30)
while True: #o professor fez diferente aqui substituindo o for por um if
    perg2 = int(input('Mostrar notas de qual aluno: (999 para interromper): '))
    if perg2 == 999:
        break
    for i, p in enumerate(boletim):
        if perg2 == i:
            print(f'As notas de {p[0]} são {p[1], p[2]}')
#   if perg2 <= len(boletim) - 1:
#       print(f'As notas de {boletim[perg2][0] são {boletim[perg2][boletim[1], boletim[2]}
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
