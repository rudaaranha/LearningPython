#Ex078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
#foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {cont}:')))
print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
print()


#COMO O PROFESSOR FEZ
#valores = []
#maior = menor = 0
#for c in range(0, 5):
#   valores.append(int(input(f'Digite um valor para posição(c): ')))
#   if c == 0:                         #SE C FOR O PRIMEIRO VALOR LIDO(POSIÇÃO O) ELE VAI SER O MAIOR E O MENOR, INDEPENDENTE DO NÚMERO
#       mai = men = valores[c]         #ASSIM, O MAIOR VAI SER IGUAL AO MENOR NA POSIÇÃO C
#   else:                              #SENÃO
#       if valores[c] > maior:         #SE OS VALORES NA POSIÇÃO C FOR MAIOR QUE O MAIOR:
#           maior = valores[c]         #O MAIOR PASSA A SER O MAIOR VALOR NA POSIÇÃO C ATUAL
#       if valores[c] < menor:         #SE OS VALORES NA POSIÇÃO C FOR MENOR QUE O MENOR:
#           menor = valores[c]         #O MENOR PASSA A SER O MENOR VALOR NA POSIÇÃO C ATUAL
#print('-='*30)
#print(f'Você digitou os valores {valores}')
#print(f'O maior valor digitado foi {maior} nas posições ', end='')           #MAIOR VALOR DIGITADO
#for i, v in enumerate(valores):          #ONDE i É A POSIÇÃO E v O VALOR OU O PRÓPRIO ELEMENTO.
#   if v == maior:                        #SE v FOR IGUAL AO MAIOR ELEMENTO:
#       print('{i}...', end='')           #PRINT FORMATADO DA POSIÇÃO DO MAIOR.
#print()
#print(f'O menor valor digitado foi {menor} nas posições ', end='')           #MENOR VALOR DIGITADO
#for i, v in enumerate(valores):
#   if v == menor:                        #SE v FOR IGUAL AO MENOR ELEMENTO:
#       print(f'{i}... ', end='')         #PRINT FORMATADO DA POSIÇÃO DO MENOR ELEMENTO
#print()