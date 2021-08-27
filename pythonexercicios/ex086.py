#Ex086 - Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for c in range(0, 9):
    if c == 0 or c == 1 or c == 2:
        n = int(input(f'Digite um valor para [0, {c}]: '))
        matriz[0].append(n)
    elif c == 3 or c == 4 or c == 5:
        n = int(input(f'Digite um valor para [1, {c - 3}]: '))
        matriz[1].append(n)
    elif c == 6 or c == 7 or c == 8:
        n = int(input(f'Digite um valor para [2, {c - 6}]: '))
        matriz[2].append(n)
print('-='*30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')

#resolução do professor:
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#for l in range(0, 3):       #l é linha
#   for c in range:          #c é coluna
#       matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#print('-='*30)
#for l in range(0, 3):
#   for c in range(0, 3):
#       print(f'[{matriz[l][c]:^5}]', end='')
#   print()
