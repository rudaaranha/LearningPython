#Ex098 -  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep
def contador(inicio, fim,  passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * -1
    print('-='*30)
    print(f'Contagem de {inicio} até {fim - 1} de {passo} em {passo}')
    if inicio < fim:
        for n in range(inicio, fim, passo):
            sleep(0.5)
            print(n, end=' ')
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont = cont - passo
        print('FIM!')


#Programa principal
contador(1, 11, 1)
contador(10, 1, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi + 1, pas)
