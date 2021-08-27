#Ex070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
#continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('-'*35)
print('{:^35}'.format('LOJA SUPER BARATÃO'))
print('-'*35)
total = prodmil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        prodmil += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {prodmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato é o(a) {barato} que custa R${menor:.2f}')
