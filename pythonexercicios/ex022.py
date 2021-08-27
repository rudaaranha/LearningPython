#Ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao tem no total sem considerar os espaços. Quantas letras tem o primeiro nome.
print('Este programa lê o nome completo de uma pessoa e mostra o mesmo com todas as letras maiúsculas, minúsculas, o número total de letras sem considerar os espaços e o número de letras do primeiro nome')
nome=str(input('Digite o seu nome completo:')).strip()
print('Analisando o nome...')
print('O seu nome é {}.'.format(nome))
print('O seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Agora apenas com letras minúsculas: {}.'.format(nome.lower()))
print('O nome {} tem ao todo {} letras'.format(nome, len(nome) - nome.count(' ')))
print('O seu primeiro nome possui {} letras.'.format(nome.find(' ')))
