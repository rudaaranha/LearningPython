#Ex044 - Elabora um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
#- À vista dinheiro: 10% de desconto;
#- À vista no cartão (débito): 5% de desconto;
#- Em até 2x no cartão: Preço normal;
#- 3x ou mais vezes no cartão: 20% de juros.
print('Este programa calcula o valor de um produto considerando a forma de pagamento.')
p = float(input('Qual o preço do produto? R$')) #preço do produto
print('''Nós possuímos quatro formas de pagamento:
[ 1 ] - À vista (10% de desconto)
[ 2 ] - Débito no cartão (5% de desconto)
[ 3 ] - Cartão de crédito em até 2x (preço normal)
[ 4 ] - Cartão de crédito em 3x ou mais (20% de juros)''')
pag = str(input('Escolha a forma de pagamento (1, 2, 3 ou 4):')) #forma de pagamento
if pag == '1':
    p1 = p - (p*10/100)
    print('Para pagamentos à vista, oferecemos 10% de desconto. Assim, o produto que custava R${:.2f} passa a custar R${:.2f}.'.format(p, p1))
elif pag == '2':
    p1 = p - (p*5/100)
    print('Para pagamentos no débito, oferecemos 5% de desconto. Assim, o produto que custava R${:.2f} passa a custar R${:.2f}.'.format(p, p1))
elif pag == '3':
    print('Para pagamentos em até 2x no cartão não oferecemos desconto, o preço é o do próprio produto, igual a R${:.2f}'.format(p))
    parcelas = str(input('O pagamento será dividido em quantas vezes, 1 ou 2?')) #número de parcelas
    if parcelas == '1':
        print('O valor a ser pago foi de R${:.2f} em uma única parcela.'.format(p))
    elif parcelas == '2':
        print('O valor a ser pago será duas vezes de R${:.2f}.'.format(p/2))
    else:
        print('Número de parcelas inválido. Por favor, tente novamente.')
elif pag == '4':
    p1 = p + (p * 20 / 100)
    print('Para pagamentos em 3x ou mais no cartão, o valor terá um acréscimo de 20%.')
    print('Desta forma, o produto custava R${:.2f}, passará a custar R${:.2f}.'.format(p, p1))
    parcelas = str(input('Em quantas vezes será feito o pagamento? (lembrando que dividimos no máximo em 6x com juros)'))
    if parcelas == '3':
        print('O valor a ser pago será três vezes de R${:.2f}.'.format(p1 / 3))
    elif parcelas == '4':
        print('O valor a ser pago será quatro vezes de R${:.2f}.'.format(p1 / 4))
    elif parcelas == '5':
        print('O valor a ser pago será cinco vezes de R${:.2f}.'.format(p1 / 5))
    elif parcelas == '6':
        print('O valor a ser pago será seis vezes de R${:.2f}.'.format(p1 / 6))
    else:
        print('Número de parcelas inválido. Por favor, tente novamente.')
else:
    print('Forma de pagamento inválida. Por favor, tente novamente.')
print('Obrigado pela preferência e volte sempre!')
