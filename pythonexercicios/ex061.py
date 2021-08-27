#Ex061 - Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
x = int(input('Primeiro termo:'))
y = int(input('Razão:'))
décimo = x + (10 - 1) * y
pa = x
cont = y
print('{} - '.format(pa), end='')
while pa < décimo:
    pa = pa + cont
    print('{}'.format(pa), end=' - ')
print('ACABOU!')

#--------------------------------------------------
#O modo que o professor fez
#print('     10 TERMOS DE UMA PA     ')
#print('='*30)
#primeiro = int(input('Primeiro termo:'))
#razão = int(input('Razão da PA:'))
#termo = primeiro
#cont = 1
#while cont <= 10:
#   print('{} - '.format(termo), end='')
#   termo += razão
#   cont += 1
#print('FIM')