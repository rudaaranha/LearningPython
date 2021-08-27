#Ex050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('Dentre o seis números, {} são pares e a sua soma é igual a {}.'. format(cont, soma))
