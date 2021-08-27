#Ex084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
pessoas = list()
nomepeso = list()
maispesado = maisleve = 0
while True:
    nomepeso.append(str(input('Nome: '))) #adicionar um nome à lista nomepeso
    nomepeso.append(float(input('Peso: '))) #adicionar um peso à lista nomepeso
    if len(pessoas) == 0:        #se o tamanho total da lista pessoas = 0, o maior peso = ao menor peso que vai ser igual ao elemento da lista nomepeso1
        maispesado = maisleve = nomepeso[1]
    else:
        if nomepeso[1] > maispesado: #determinar o de maior peso
            maispesado = nomepeso[1]
        if nomepeso[1] < maisleve:   #determinar o mais leve
            maisleve = nomepeso[1]
    pessoas.append(nomepeso[:])  # copiar os elementos da lista nomepeso para lista pessoas
    nomepeso.clear()                      #limpar a lista nomepeso antes de outra repetição do laço
    perg = ' '
    while perg not in 'SN':               #evitar que respostas fora do S/N sejam aceitas pelo programa
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':          #condição de parada do laço
        break
print('-='*30)
print(f'A) Ao todo você cadastrou {len(pessoas)} pessoas.') #tamanho da lista pessoas vai determinar quantos foram cadastrados
print(f'B) O maior peso foi {maispesado}Kg. Peso de ', end='')
for p in pessoas:         #laço para determinar se mais de uma pessoa foi cadastrada com maior peso
    if p[1] == maispesado:
        print(f'{p[0]} ', end='')
print()
print(f'C) O menor peso foi {maisleve}Kg. peso de ', end='')
for p in pessoas:        #repetindo o laço para as pessoas de menor peso
    if p[1] == maisleve:
        print(f'{p[0]} ', end='')
print()
