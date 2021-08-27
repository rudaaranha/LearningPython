#Ex033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('Este programa lê 3 números e diz qual é o menor e o maior.')
print('Sendo assim...')
a=int(input('Digite o primeiro número:'))
b=int(input('Agora digite o segundo número:'))
c=int(input('Por fim, digite o terceiro número:'))
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor =  b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))
