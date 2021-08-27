#Ex095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
#detalhes do aproveitamento de cada jogador
jogadores = []
dados = dict()
gols = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    gols.clear()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for g in range(0, partidas):
        ngols = (int(input(f'Quantos gols na partida {g + 1}? ')))
        gols.append(ngols)
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-='*30)
print(jogadores)
print('-='*30)
print('cod', f'{"Nome":>5}', f'{"gols":>12}', f'{"Total":>10}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i + 1}     ', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='  ')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols.')
        print('-'*40)
print('<< VOLTE SEMPRE >>')


#print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
#for i, v in enumerate(gols):
    #print(f'  => Na partida {i + 1}, fez {v} gols.')
#print(f'Foi um total de {sum(gols)} gols.')
