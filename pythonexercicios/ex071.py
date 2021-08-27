#Ex071 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
#o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{:^30}'.format('BANCO RUDAZIN'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédula = 50 #A maior cédula do real é 100, mas o enunciado mandou considerar até 50.
totalcédulas = 0 #total de cédulas que o programa vai fornecer ao usuário, ou seja, contagem de cédulas
while True:
    if total >= cédula:  #Se o valor total foi maior ou igual à maior cédula (R$50)
        total = total - cédula #O novo valor total vai ser igual ao valor total antareior menos o valor da cédula (repete quantas vezes for necessário)
        totalcédulas = totalcédulas + 1 #A cada repetição, uma cédula é contada.
    else:
        if totalcédulas > 0:
            print(f'Total de {totalcédulas} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédulas = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO RUDAZIN. Tenha um bom dia!')
