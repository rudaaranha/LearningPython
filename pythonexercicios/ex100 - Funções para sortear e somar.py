#Ex100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = []
pares = []


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        numeros.append(n)
    print('PRONTO!')


def somapar():
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    print(f'Somando os valores pares de {numeros}, temos {sum(pares)}')


sorteia()
somapar()


#RESOLUÇÃO DO PROFESSOR

#from random import randint


#def sorteia(lista):
#    print(f'Sorteando 5 valores da lista: ', end='')
#    for cont in range(0, 5):
#        n = randint(0, 10)
#        print(n, end=' ')
#        lista.append(n)
#    print('PRONTO!')


#def somapar(lista):
#   soma = 0
#   for valor in lista:
#       if valor % 2 == 0:
#           soma = soma + valor
#   print(f'Somando os valores pares de {lista}, temos {soma}')


#numeros = list()
#sorteia()
#somapar()