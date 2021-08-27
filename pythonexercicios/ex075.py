#Ex075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
w = int(input('Digite o terceiro número: '))
z = int(input('Digite o último número: '))
num = (x, y, w, z)
print('-='*30)
print(f'Você digitou os seguintes valores: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nA) O número nove aparece {num.count(9)} vezes.')
print('-='*30)
if 3 in num:
    print(f'B) O número 3 apareceu pela primeira vez na {num.index(3)+1}ª posição.')
else:
    print(f'B) O número 3 não foi digitado nenhuma vez.')
print('-='*30)
print('C) Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('\nFIM')
