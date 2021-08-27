#Ex091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #sorted jogadores.itens pra deixar em ordem, key=itemgetter(1) para os valores sorteados que devem ficar em ordem e reverse pra ser decrescente
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)



#jogadores['jogador1'] = randint(1, 6)
#jogadores['jogador2'] = randint(1, 6)
#jogadores['jogador3'] = randint(1, 6)
#jogadores['jogador4'] = randint(1, 6)
#dados.append(jogadores['jogador1'])
#dados.append(jogadores['jogador2'])
#dados.append(jogadores['jogador3'])
#dados.append(jogadores['jogador4'])
#dados.sort(reverse=True)
#for k, v in jogadores.items():
#   print(f'O {k} tirou {v}')
#print('Ranking dos jogadores:')
#for i, v in enumerate(dados):
#    print(f'{i + 1}° lugar: {k} com {v}')