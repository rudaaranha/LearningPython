#Ex007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
print('Este programa calcula a média de um aluno a partir das suas notas')
aluno=input('Digite o nome do aluno:')
n1=float(input('Digite a primeira nota do(a) {}:'.format(aluno)))
n2=float(input('Digite a segunda nota do(a) {}:'.format(aluno)))
media=(n1+n2)/2
print('A média do(a) {} baseada nas suas notas foi {:.2f}.'.format(aluno, media))
