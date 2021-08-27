#Ex093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
#e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
gols = []
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for g in range(0, partidas):
    ngols = (int(input(f'Quantos gols na partida {g + 1}? ')))
    gols.append(ngols)
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'  => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
