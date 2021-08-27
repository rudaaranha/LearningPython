#Ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário e diga se elas podem ou não formar um triângulo.
print('Este programa lê o comprimento de três retas e diz se elas podem formar um triângulo.')
r1 = float(input('Qual o comprimento da primeira reta em mm?'))
r2 = float(input('E da segunda reta?'))
r3 = float(input('E da terceira reta?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR um triânulo!')
