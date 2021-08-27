#Ex027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('Esse programa lê o nome completo de uma pessoa e mostra seu primeiro e último nome separadamente.')
n=str(input('Qual o seu nome completo?')).strip()
nome=n.split()
print('Muito prazer em te conhecer {}!'.format(nome[0]))
print('Seu primeiro nome é {}.'.format(nome[0]))
print('E seu último nome é {}'.format(nome[len(nome)-1]))
