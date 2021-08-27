#Ex101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
#nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
#NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano):
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade <= 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    return


#Programa principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
