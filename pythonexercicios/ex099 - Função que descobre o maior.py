#Ex099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        sleep(0.5)
        print(n, end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont = cont + 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print((f'O maior valor informado foi {maior}.'))


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
