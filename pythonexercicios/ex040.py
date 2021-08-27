#Ex040 - Crie um programa que leia duas notas de um aluno e calcule uma média, mostrando uma mensagem no final, de acordo com a média atingida.
#- Média abaixo de 5.0: REPROVADO;
#- Média entre 5.0 e 6.9: RECUPERAÇÃO;
#- Média 7.0 ou superior: APROVADO.
print('Este programa calcula a média final de um aluno e diz se o mesmo foi aprovado, reprovado ou está em recuperação.')
nome = str(input('Aluno(a):'))
nota1 = float(input('Qual é o valor da primeira nota?'))
nota2 = float(input('Qual é o valor da segunda nota?'))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Como a média foi {:.1f}, {} está REPROVADO(A)! Estude mais.'.format(media, nome.upper()))
elif media >= 5.0 and media <= 6.9:
    print('Como a média foi {:.1f}, {} está em RECUPERAÇÂO!'.format(media, nome.upper()))
else:
    print('''Como a média foi {:.1f}, {} foi APROVADO(A). 
Parabéns {}!'''.format(media, nome.upper(), nome.upper()))
print('Tenha um bom dia!')
