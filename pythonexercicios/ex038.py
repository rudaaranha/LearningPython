#Ex038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#-O primeiro valor é maior;
#-O segundo valor é maior;
#-Não existe valor maior, os dois são iguais;
print('Este programa lê dois números inteiros e compara-os mostrando quem é o maior entre os dois ou se são iguais.')
n1 = int(input('Qual o primeiro número?'))
n2 = int(input('Qual o segundo número?'))
if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({}).'.format(n1, n2))
elif n2 > n1:
    print('O segundo número ({}) é maior que o primeiro ({}).'.format(n2, n1))
else:
    print('Os número são iguais.')
