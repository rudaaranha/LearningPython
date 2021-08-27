#Ex015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.
print('Este programa calcula o custo de um carro alugado de acordo com a quantidade de dias e a quilometragem percorrida.')
print('-'*70)
print('O custo do aluguel é de R$60.00 por dia e R$0.15 por km percorrido.')
print('-'*70)
dia=int(input('Digite o número de dias em que o carro foi alugado:'))
km=int(input('Digite a quantidade de km percorridos durante o período do aluguel:'))
custo=(dia*60.00)+(0.15*km)
print('O custo do aluguel do carro por {} dias e {}km percorridos é de R${:.2f}.'.format(dia,km,custo))
