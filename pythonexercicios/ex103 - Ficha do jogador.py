#Ex103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')


#programa principal
nome = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)
