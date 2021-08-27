# Ex020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

print('Este programa sorteia a ordem de apresentação dos alunos.')
n1 = str(input('Quem é o primeiro aluno?'))
n2 = str(input('E o segundo?'))
n3 = str(input('E o terceiro?'))
n4 = str(input('E o quarto?'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
