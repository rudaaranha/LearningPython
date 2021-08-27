#Ex025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('Este programa lê seu nome completo diz se ele possui a palavra silva.')
nome = str(input('Qual o seu nome completo?')).strip()
print('É verdade que você tem a palavra Silva no nome?')
print('silva' in nome.lower())
