#Ex011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
#área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
print('Este programa calcula a área de uma parede e a quantidade de tinta necessária para pintá-la.')
print('-'*70)
print('É bom lembrar que cada litro de tinta pinta 2m²')
print('-'*70)
l=float(input('Digita a largura de parede em metros:'))
h=float(input('Digite a altura da parede em metros:'))
a=l*h
t=a/2
print('A área da parede é {:.2f}m². \nA quantidade de tinta necessária para pintá-la é de {:.1f}l.'. format(a,t))
