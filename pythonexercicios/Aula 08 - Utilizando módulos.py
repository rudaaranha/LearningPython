#Aula 08 - Utilizando módulos (exercícios 016 até 021).
#utilizar "import math" ou "from math import sqrt" (ou qualquer outra funcionalidade...)
#ceil arredonda pra cima, enquanto floor arredonda para baixo [ex: .format(num, floor(raiz))]
#Para saber quais bibliotecas estão disponíveis, é só ir no site pyhton.org (lá inclusive tem exemplos de uso das mesmas)
#Uma biblioteca pode ser criada por qualquer um e ser disponibilizada na internet.
#Se a biblioteca não estiver no computador (ex emoji), não poderá ser importada. Porém, pelo próprio pycharm é possível baixar(e importar)

print('-'*130)
#como calcular a raiz quadrada de um número utilizando o módulo math
from math import sqrt
num=int(input('Digite um número:'))
raiz=sqrt(num)
print('A raiz quadrada do número {} é igual a {:.2f}.'.format(num,raiz))

print('-'*130)
#esse código faz com que a "máquina" diga um número aleatório float entre 0 e 1
import random
n1=random.random()
print(n1)

print('-'*130)
#esse código faz a "máquina" escolher um número entre 1 e 10
import random
n2=random.randint(1,10)
print(n2)

print('-'*130)

import emoji
print(emoji.emojize('Olá Mundo! :earth_americas:', use_aliases=True)) #colocar emojis no programa
