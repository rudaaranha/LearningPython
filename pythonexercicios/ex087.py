#Ex087 - Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[], [], []]
pares = []
maior = menor = 0
#scol3 = 0
for c in range(0, 9):
    if c == 0 or c == 1 or c == 2:
        n = int(input(f'Digite um valor para [0, {c}]: '))
        matriz[0].append(n)
        if n % 2 == 0:
            pares.append(n)
    elif c == 3 or c == 4 or c == 5:
        n = int(input(f'Digite um valor para [0, {c - 3}]: '))
        matriz[1].append(n)
        if n % 2 == 0:
            pares.append(n)
        if n > maior:
            maior = n
    elif c == 6 or c == 7 or c == 8:
        n = int(input(f'Digite um valor para [0, {c - 6}]: '))
        matriz[2].append(n)
        if n % 2 == 0:
            pares.append(n)
print('-='*30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print('-='*30)
print(f'A) A soma dos valores pares é {sum(pares)}.')
print(f'B) A soma dos valores da terceira coluna é {matriz[0][2] + matriz [1][2] + matriz[2][2]}.')
#for l in range(0, 3):
#    scol3 = scol3 + matriz[l][2]
#print(f'B) A soma dos valores da terceira coluna é {scol3}')
print(f'C) O maior valor da segunda linha é {maior}.')

#resolução do professor:
#spar = maior = scol = 0
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#for l in range(0, 3):       #l é linha
#   for c in range:          #c é coluna
#       matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#print('-='*30)
#for l in range(0, 3):
#   for c in range(0, 3):
#       print(f'[{matriz[l][c]:^5}]', end='')
#       if matriz[l][c] % 2 == 0:
#           spar += matriz[l][c]
#   print()
#print('-='*30)
#print(f'A) A soma dos valores pares é {spar}.')
#for l in range(0,3):
#   scol += matriz[l][2]        #a coluna 2 é fixa
#print(f'B) A soma dos valores da terceira coluna é {scol}')
#for c in range(0, 3):
#   if c == 0:        #primeiro valor da linha
#       maior = matriz[1][c]    #linha 1 fixa
#   elif matriz[1][c] > maior:
#       maior = matriz[1][c]    #linha 1 fixa
#print(f'C) O maior valor da segunda linha é {maior}.')
