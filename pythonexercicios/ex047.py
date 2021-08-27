#Ex047 - Crie um programa que mostre na tela todos os número pares que estão no intervalo entre 1 e 50.
print('Este programa mostra todos os números pares no intervalo entre 1 e 50.')
for n in range(2, 51, 2):
    print(n, end=' ')
print('FIM.')

#outra forma de fazer, porém que requer mais do computador é:
#for n in range(1, 51):
#   if n % 2 == 0:
#       print(n, end=' ')
#print('FIM.')