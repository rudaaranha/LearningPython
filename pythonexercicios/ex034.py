#Ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários maiores que R$1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%
print('Este programa calcula um aumento baseado no salário do funcionário.')
print('Para salários acima de R$1.250,00, o aumento é de 10%, para salários inferiores ou iguais, o aumento é de 15%.')
sal=float(input('Qual o seu salário atual? R$'))
aumento1 = sal + (sal * 0.1)
aumento2 = sal + (sal * 0.15)
if sal > 1250.00:
    print('Seu novo salário é R${:.2f}.'.format(aumento1))
else:
    print('Seu novo salário é R${:.2f}.'.format(aumento2))

#outra forma de escrever esse programa
#sal=float(input('Qual o seu salário atual? R$'))
#if sal <= 1250:
#   novo = sal + (sal * 0.1)
#else:
#   novo = sal + (sal * 0.15)
#print('Quem ganhava {:.2f}, passou a ganhar {:.2f}'.format(sal, novo))
