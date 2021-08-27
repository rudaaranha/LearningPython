#AULA TEÓRICA
#É a estrutura de repetição mais simples. Faz com que as repetições sejam reduzidas. ou que as repetições sejam simplificadas, feitas automaticamente.
#Estrutura de repetição com variável de controle.
# a forma de escrever seria
#for c in range(1,10):
#   passo
#pega.
#for é o camando de repetição, c é a variável, in é "no" (tradução literal) e range é intervalo.
#Condições(if) podem ser adicionadas dentro da estrutura de repetição (for) e vice versa.

#-------------------------------------------------------------------------------------------------

#AULA PRÁTICA
# para escrever "oi" 6 vezes, teria que repetir print('oi') 6 seis vezes ou pode usar uma estrutura de repetição mostrada abaixo.
for c in range(0, 6): #tem que ser de 0 a 6 para que o python repita seis vezes. de 1 a 6 ele não reconhece o sexta repetição.
    print('Oi')
print('FIM.')

print('-' * 40)
#se for dado um tab no print('FIM') ele vai ser repetido 6x também.
for c in range(0, 6):
    print('Oi')
    print('FIM.')

print('-' * 40)
#se quiser fazer uma contagem de 1 até 6, tem que fazer o print(c) e mudar o range para (1, 7) pois o último não é reconhecido pelo python
for c in range(1, 7):
    print(c)
print('FIM.')

print('-' * 40)
#se quiser contar ao contrário, inverte os números e tem que adicionar o -1 no range para ele entender que tipo de iteração está sendo feita.
# e não precisa adicionar um número a mais começar do "7".
for c in range(6, 0, -1):
    print(c)
print('FIM.')

print('-' * 40)
#Ao contar de 0 a 6 e for adicionado um dois ao range, o programa vai contar de 2 em 2.
for c in range(0, 7, 2):
    print(c)
print('FIM.')

print('-' * 40)
#pode ser feita uma contagem utilizando o comando input, ou seja, a pessoa escolhe um número e o programa faz a contagem baseado no número escolhido.
n = int(input('Digite um número: '))
for c in range(0, n+1): #nesse caso se coloca o n+1 pois o python não reconhece o último número.
    print(c)
print('FIM.')

print('-' * 40)
#tudo pode ser escolhido pela pessoa... ou seja, o inicio, o fim e o passo da contagem.
i = int(input('Inicio: '))
f = int(input('Fim: '))
p =int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM.')

print('-' * 40)
#Se o input vier dentro do comando for, por exemplo, para digitar um número... o pedido para digitar um número vai ser repetido o número de vezes do range pré determinado.
#ou seja, a pessoa terá que digitar um número qualquer pelo número de vezes do range.
for c in range(0, 3):
    n = int(input('Digite um número: '))
print('FIM.')

print('-' * 40)
#repetindo o exemplo anterior, mas fazendo um somatório dos números escolhidos
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s = s + n #somatório. Que também pode ser escrito como "s += n".
print('O somatório de todos os valores foi {}.'.format(s))

print('FIM. É O FIM MESMO.')
