#Ex090 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
print('-='*30)
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos['Média'] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'  - {k} é igual a {v}')
