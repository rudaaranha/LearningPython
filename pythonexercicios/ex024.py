#Ex024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
print('Este programa lê um nome de uma cidade e diz se ela começa com a palavra "santo"')
cidade=str(input('Digite o nome de uma cidade:')).strip()
print('É verdade que a cidade de {} possui a palavra Santo no nome?'.format(cidade))
print(cidade[:5].upper() == 'SANTO')
