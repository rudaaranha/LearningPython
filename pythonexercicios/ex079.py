#Ex079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Tente outro valor...')
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg in 'nN':
        break
print(f'A lista formada em ordem crescente foi: {sorted(num)}.')