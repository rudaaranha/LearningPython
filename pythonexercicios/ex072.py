#Ex072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze', 'quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {num[n]}.')
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if pergunta == 'S':
        print('Vamos continuar.', end=' ')
        while True:
            n = int(input('Digite um número entre 0 e 20: '))
            if 0 <= n <= 20:
                break
            print('Tente novamente.', end=' ')
        print(f'Você digitou o número {num[n]}.')
    if pergunta == 'N':
            break
print('Até mais.')
