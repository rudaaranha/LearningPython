#Aula 07 - Operadores aritméricos (exercícios 005 até 015).
n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s=n1+n2
sub=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}.'.format(s, m, d), end=' Do mesmo jeito que a ')
print('subtração é {}, divisão inteira é {} e a potência é {}.'.format(sub, di, e))
