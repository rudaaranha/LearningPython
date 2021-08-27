#Ex060 - Faça um programa que leia um número qualquer e mostre seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#----------------------------------------------------------------------------
#MODO TRADICIONAL USANDO WHILE

print('Este programa realiza o Cálculo Fatorial de um número inteiro "n".')
print('-=-'*10)
n = int(input('Digite um número:')) #leia o valor de n
c = n #Vamos iniciar com o contador sendo que este vai iniciar com o valor de n. P/ ex: se n = 5, o fatorial de 5, começa com 5 (5! = 5x4x3x2x1)
fat = 1 #Uma vez que o fator nulo de multiplicação é igual a 1.
print('Calculando {}! = '.format(n), end='')
while c > 0: #nesse ponto c tem que ser maior que 0 pois não tem como realizar fatorial de número negativo.
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * c #cálculo do fatorial
    c -= 1 #c = c - 1 (vai garantir que em cada laço, a variável c seja 1 a menos quando comparado com o laço anterior)
print('{}'.format(fat))

#Explicando o programa: enquanto c > 0, o laço se repete... uma vez que n é sempre maior que zero, ao utilizar o while, o cálculo
#fat = fat * c vai se repetir até que o c seja igual a zero e o qua vai garantir que esse cálculo vai funcionar bem são as linhas
#c = n (explicado na linha 10) e c = c - 1 (c sempre vai diminuir 1 a medida que o laço se repete e ele seja maior que 0).

#---------------------------------------------------------------------------------------------

#MODO SIMPLES IMPORTANDO A BIBLIOTECA FATORIAL

#from math import factorial
#n = int(input('Digite um número:')) #leia o valor de n
#f = factorial(n)
#print('O Fatorial do número {} é igual a {}.'.format(n, f))
