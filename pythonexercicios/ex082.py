#Ex082 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
#crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')
