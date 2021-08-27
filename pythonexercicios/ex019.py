#Ex019 - Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome dos alunos e sorteando o escolhido.
from random import choice
print('Este programa sorteia um nome aleatório de uma lista.')
n1=str(input('Quem é o primeiro aluno?'))
n2=str(input('E o segundo?'))
n3=str(input('E o terceiro?'))
n4=str(input('E o quarto?'))
lista = [n1, n2, n3, n4]
choice(lista)
print('O(a) aluno(a) escolhido(a) foi:'.format(choice))
