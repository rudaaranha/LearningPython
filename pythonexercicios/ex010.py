#Ex010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1.00=R$4.20
print('Este programa determina a quantidade dólares que podem ser comprados com o que você tem na carteira.')
c=float(input('Digite quanto de dinheiro você tem na carteira em R$:'))
d=c/4.20
print('Como você possui R${:.2f} na carteira, é possível comprar US${:.2f}.'.format(c,d))
