#Ex106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
#comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
#o programa se encerrará. Importante: use cores.
from time import sleep
cores = {'semcor': '\033[m',       # semcor - sem cor
         'vm': '\033[0;30;41m',    # vm - vermelho
         'vd': '\033[0;30;42m',    # vd - verde
         'am': '\033[0;30;43m',    # am - amarelo
         'az': '\033[0;30;44m',    # az - azul
         'rx': '\033[0;30;45m',    # rx - roxo
         'br': '\033[7;30m',       # br - branco
         }


def titulo(msg2, cor=0):
    tam = len(msg2) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg2}')
    print('~'*tam)
    print(cores['semcor'], end='')
    sleep(1)


def pyhelp(msg):
    titulo(f'Acessando o manual do comando \'{msg}\'', 'az')
    print(cores['br'], end='')
    help(msg)
    print(cores['semcor'], end='')
    sleep (1)


#Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'rx')
    ajuda = str(input('Função ou Biblioteca > '))
    if ajuda.upper() == 'FIM':
        break
    pyhelp(ajuda)
titulo('ATÉ LOGO!', 'vm')
