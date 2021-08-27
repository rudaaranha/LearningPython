#Ex039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar no serviço militar;
#-Se é a hora de se alistar;
#-Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('Este programa determina quanto tempo falta, se está no tempo ou se já passou o tempo para uma pessoa fazer o alistamento militar.')
sexo = str(input('Qual o seu sexo? Digite "M" para masculino e "F" para feminino: '))
if sexo.upper() == 'M':
    ano = int(input('Ano de nascimento:'))
    atual = date.today().year
    idade = atual - ano
    alistamento = atual + (18 - idade)
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
    if idade < 18: #condição dentro da condição.
        alistamento1 = atual + (18 - idade)
        print('Seu alistamento será em {}.'.format(alistamento1))
    elif idade == 19:
        print('Você deveria ter se alistado ano passado.')
    elif idade > 18 and idade != 19:
        alistamento2 = atual - (idade - 18)
        print('Você deveria ter se alistado em {}, ou seja, há {} anos.'.format(alistamento2, idade-18))
    else: #poderia utilizar mais um elif ao invés do else.
       #elif idade == 18:
        print('Seu alistamento é neste ano de {}. ALISTE-SE JÁ!'.format(atual))
elif sexo.upper() == 'F':
    print('Você não precisa fazer o alistamento militar!')
else:
    print('Caractere inválido. Por favor, tente novamente.')
print('Tenha um bom dia!')
