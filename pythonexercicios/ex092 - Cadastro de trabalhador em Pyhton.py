#Ex092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento:'))
atual = date.today().year
cadastro['idade'] = atual - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    inicioservico = cadastro['ano de contratação'] - nascimento
    cadastro['aposentadoria'] = inicioservico + 35
print('-='*30)
print(cadastro)
for k, v in cadastro.items():
    print(f'  - {k} tem valor {v}')
