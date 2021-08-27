#Ex065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos os valores
#e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
pergunta = 'Ss'
soma = média = cont = maior = menor = 0
while pergunta != 'N':
    n = int(input('Digite um número: '))# Não precisa definir n fora do laço porque ele não é a variável do laço  (pergunta é a variável)
    cont = cont + 1 #contagem de repetições do laço
    soma = soma + n #soma entre os valores digitados
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    pergunta = str(input('Você quer continuar digitando valores? [S/N]')).upper().strip()[0]
média = soma/cont #média dos valores digitados (vai ser a soma dos valores dividido pela contagem)
print('A média entre os valores digitados é {}.'.format(média))
print('O maior número é {} e o menor número foi {}.'.format(maior, menor))
