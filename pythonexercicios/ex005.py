#Ex005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
print('Este é um programa que mostra o número sucessor e o número antecessor de um número inteiro qualquer. \nSendo assim...')
n=int(input('Digite um número:'))
suc=n+1
ant=n-1
print('Para o número {}, temos que seu sucessor é {} e seu antecessor é {}!'.format(n, suc, ant))
