#Ex058 - Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar advinhar tal número
#até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
print('-----Jogo da adivinhação-----')
print('Será que você consegue adivinha o número que eu estou pensando de 0 a 10??')
sleep(2)
print('Vamos tentar...')
sleep(2)
computador = randint(0, 10) #comando que faz o computador escolher um número aleatório entre 0 e 5.
print('Eu vou pensar em um número entre 0 e 10, tente advinhar qual foi.')
print('Um momento...')
sleep(1)
print('Pronto')
jogador = int(input('Qual número eu pensei?'))  #Jogador tenta adivinhar o número
contagem = 1 #número de tentativas de acertar o número. Começa em uma porque a pessoa pode acertar de primeira.
while jogador != computador: #enquanto a variável jogador for diferente da variável computador:
    if jogador < computador:
        jogador = int(input('Quase... tente um número maior: '))
    elif jogador > computador:
        jogador = int(input('Quase.... tente um número menor: '))
    contagem += 1  # contagem de tentativas de acerto dentro do laço
print('PARABÉNS! Você acertou e precisou de {} tentativas para isto.'.format(contagem))

#COMO O PROFESSOR FEZ
#from random import randint
#computador = randint(0, 10)
#print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
#print('Será que você consegue advinhar qual foi?')
#acertou = False
#palpites = 0
#while not acertou:
#   jogador = int(input('Qual o seu palpite? '))
#   palpites += 1
#   if jogador == computador:
#       acertou = True
#   else:
#       if jogador < computador:
#           print('Mais... Tente novamente.')
#       elif jogador > computador:
#           print('Menos... Tente novamente.')
#print('Acertou com {} tentativas. Parabéns!'.format(palpites))