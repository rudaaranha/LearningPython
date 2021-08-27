#Ex054 - Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já
#são maiores.
from datetime import date
atual = date.today().year
totmaior = 0 #número de pessoas maior de idade começando do zero
totmenor = 0 #número de pessoas menor de idade começando do zero
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    #print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 18:
        totmaior += 1 #vai somando uma pessoa ao montante dependendo da idade
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))