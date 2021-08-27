#Ex046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 com uma pausa de 1 segundo entre eles.
from time import sleep
print('Este programa faz uma contagem regressiva para o ano novo quando estiver faltando 10 segundos.')
for c in range(10, -1, -1): #aqui tem que colocar o -1 na segunda posição pois o python exclui o último número.
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')
