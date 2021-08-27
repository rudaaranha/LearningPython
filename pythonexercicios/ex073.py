#Ex073 - Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
#Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Flamengo.
brasileiro = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Internacional', 'Grêmio', 'Fluminense', 'Santos',
              'Atlético-GO', 'Corinthians', 'Ceará', 'Bragantino', 'Fortaleza', 'Athletico-PR', 'Sport',
              'Bahia', 'Vasco', 'Coritiba', 'Goiás', 'Botafogo')
print(f'A) Os primeiros cinco colocados na rodada 26 são: {brasileiro[:5]}.')
print('-='*60)
print(f'B) Os últimos quatro colocados do brasileiro depois de 26 rodadas são: {brasileiro[-4:]}.') #{brasileiro[16:20]}
print('-='*60)
print(f'C) {sorted(brasileiro)}')
print('-='*60)
print(f'D) O {brasileiro[2]} está na {brasileiro.index("Flamengo") + 1}ª posição.')
