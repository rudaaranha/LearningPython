#Ex026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que
# posição ela aparece a última vez.
print('Este programa lê uma frase e diz quantas letras "A" aparecem e as posições que ela aparece pela primeira e última vez.')
frase=str(input('Digite uma frase:')).upper()
print('A letra A aparece {} vez(es) na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" apareceu foi na posição {}'.format(frase.rfind('A')+1))
