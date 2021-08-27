#Ex013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
print('Este algoritmo mostra o salário de um funcionário com 15% de aumento')
f=input('Qual o nome do(a) funcionário(a)?')
s=float(input('Digite o salário atual do funcionário em reais:'))
p=s+(s*(15/100))
print('O salário de {} que era R${:.2f}, passou a ser de R${:.2f}.'.format(f,s,p))
