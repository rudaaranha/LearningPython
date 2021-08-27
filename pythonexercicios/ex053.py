#Ex053 - Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite uma frase:')).strip().upper() #strip elimina os espaços antes e depois da frase.
palavras = frase.split() #comando para fatiar a frase.
junto = ''.join(palavras) #comando para juntar as palavras numa só (eliminando os espaços).
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #vai pegar o número de letras da variável "junto" e vai tirar uma, se você tiver 20 letras não é do 1 ao 20 e sim
#do zero ao 19 (primeiro -1). vai até a letra -1, antes da primeira (segundo -1). voltando uma letra de cada vez, contagem de trás para frente (terceiro -1).
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#Outro forma de fazer:
#frase = str(input('Digite uma frase:')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = junto[::-1]
#print('O inverso de {} é {}.'.format(junto, inverso))
#if inverso == junto:
#    print('Temos um palíndromo!')
#else:
#    print('A frase digitada não é um palíndromo!')
