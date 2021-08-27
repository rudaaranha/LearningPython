#Ex069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('=======CADASTRO DE PESSOAS=======')
pessoas = homens = mulheres = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        pessoas = pessoas + 1
    if sexo == 'M':
        homens = homens + 1
    if idade < 20 and sexo == 'F':
        mulheres = mulheres + 1
    print('-'*30)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print('=======FIM DO PROGRAMA=======')
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homens} pessoas do sexo masculino cadastrado(s).')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos.')
