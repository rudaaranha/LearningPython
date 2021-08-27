#Ex081 - Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
num = []
while True:
    num.append(int(input('Digite um valor: ')))
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print('-=' * 30)
print(f'A) Foram digitados {len(num)}.')
num.sort(reverse=True)
print(f'B) A lista gerada em ordem decrescente foi {num}')
if 5 in num:
    print(f'C) O número 5 faz parte da lista e apareceu {num.count(5)} vezes.')
else:
    print('C) O número 5 não faz parte da lista.')
