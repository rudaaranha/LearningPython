#Ex041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM;
#- Até 14 anos: INFANTIL;
#- Até 19 anos: JÚNIOR;
#- Até 25 anos: SÊNIOR;
#- Acima: MASTER.
from datetime import date
print('Este é um programa que determina a categoria de um atleta de acordo com sua idade.')
print('Para isto é necessário se cadastrar informando o nome e idade.')
nome = str(input('Qual o seu nome?'))
atual = date.today().year #ano atual.
ano = int(input('Qual seu ano de nascimento?'))
idade = atual - ano
print('{}, você nasceu em {}, portanto tem {} anos.'.format(nome, ano, idade))
if idade <= 9:
    print('Você pertence à categoria MIRIM.')
elif 10 <= idade <= 14:
    print('Você pertence à categoria INFANTIL.')
elif 15 <= idade <= 19:
    print('Você pertence à categoria JÚNIOR.')
elif 20 <= idade <= 25:
    print('Você pertence à categoria SÊNIOR.')
elif idade > 25:
    print('Você pertence à categoria MASTER.')
