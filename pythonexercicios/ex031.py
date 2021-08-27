#Ex031 - Desenvolva um programa que lê a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km
#para viagens de até 200km e R$0.45 para viagens mais longas.
print('Este programa calcula o preço de uma passagem baseada na distância a ser percorrida.')
print('Para viagens de até 200km, será cobrado um valor de R$0.50 por quilometro.')
print('Se a viagem for mais longa, será cobrado um valor de R$0.45 por quilometro.')
dist=float(input('Digite a distância da viagem em quilometros(km):'))
vc=dist*0.50
vl=dist*0.45
if dist <= 200:
    print('O valor da sua passagem será de R${:.2f}.'.format(vc))
else:
    print('O valor da sua passagem será de R${:.2f}.'.format(vl))
