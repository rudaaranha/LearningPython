#Ex028 - Escrevam um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador. O computador deve escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-----Jogo da adivinhação-----')
print('Será que você consegue adivinha o número que eu estou pensando de 0 a 5??')
sleep(2)
print('Vamos tentar...')
sleep(2)
computador = randint(0, 5) #comando que faz o computador escolher um número aleatório entre 0 e 5.
print('Eu vou pensar em um número entre 0 e 5, tente advinhar qual foi.')
print('Um momento...')
sleep(3)
print('Pronto')
sleep(1)
jogador=int(input('Qual número eu pensei?')) #Jogador tenta adivinhar o número
if jogador == computador:
    print('PARABÉNS! Você venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
