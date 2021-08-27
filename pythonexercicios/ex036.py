#Ex036 - Escreva um programa para aprovar o empréstismo para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário do comprador ou o empréstimo será negado.
print('Este programa calcula a prestação mensal de empréstimos baseado no salário do comprador. É importante salientar quem em certos casos o empréstimo é negado.')
imovel = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o salário do comprador? R$'))
ano = int(input('Em quantos anos será realizado o financiamento?'))
meses = ano*12
prestacao = imovel/meses
print('Para pagar um imóvel de R${:.2f} em {} anos...'.format(imovel, ano), end='')
print(' a prestação será de R${:.2f}.'.format(prestacao))
if prestacao <= sal*30/100:
    print('Considerando tais condições o empréstimo pode ser CONCEDIDO.')
else:
    print('Infelizmente para estas condições o empréstimo será NEGADO.')
