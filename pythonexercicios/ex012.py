#Ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print('Este algoritmo mostra o preço de um produto com 5% de desconto.')
prod=input('Qual é o produto?')
p=float(input('Digite o preço atual do produto em reais:'))
d=p-(p*(5/100))
print('O(a) {} que custa R${:.2f}, passa a custar R${:.2f} com 5% de desconto.'.format(prod,p,d))
