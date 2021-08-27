#Ex051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA(prograssão aritmética). No final mostre os 10 primeiros termos dessa PA.
print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
x = int(input('Primeiro termo:'))
y = int(input('Razão:'))
décimo = x + (10 - 1) * y
for pa in range(x, décimo + y, y): #x é o primeiro termo e y é a razão da PA.
    print('{}'.format(pa), end=' - ')
print('ACABOU!')