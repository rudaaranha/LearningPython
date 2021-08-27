#Ex029 - Escreva um programa que a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 para cada km/h acima do permitido.
from time import sleep
print('Este é um programa para fiscalização de velocidade.')
sleep(3)
print('A medição da velocidade é realizada e se esta for maior que 80km/h, o condutor é multado.')
sleep(3)
vel=float(input('Qual é a velocidade do carro em Km/h?'))
multa=(vel-80)*7
if vel > 80:
    print('Você está acima do limite de velocidade. O valor da sua multa é R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')


