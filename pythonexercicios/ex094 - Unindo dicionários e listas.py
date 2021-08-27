#Ex094 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
#pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
dados = dict()
pessoas = list()
soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma = soma + dados['idade']
    perg = ' '
    pessoas.append(dados.copy())
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
media = soma / len(pessoas)
print('-='*30)
print(f'A) - O grupo tem {len(pessoas)} pessoas.')
print(f'B) - A média de idade é de {media:.2f} anos.')
print(f'C) - As mulheres cadastradas foram: ', end='')
for m in pessoas:
    if m['sexo'] == 'F':
        print(f'{m["nome"]}', end= ' ')
print()
print('D) - Lista das pessoas com idade acima da médias: ')
for p in pessoas:
    if p['idade'] > media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
