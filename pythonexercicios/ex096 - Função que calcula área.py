#Ex096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {w}mX{l}m é de {area}m².')


#Programa principal
print('Controle de Terrenos')
print('-'*20)
w = float(input('LARGURA (m): '))
l = float(input('COMPRIMENTO (m): '))
area(w, l)
