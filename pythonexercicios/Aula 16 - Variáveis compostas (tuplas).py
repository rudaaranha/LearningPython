#AULA TEÓRICA - Variáveis compostas (tuplas)
#Em python existem 3 tipos de variáveis compostas - Tuplas, listas e dicionários.
#O simbolo "=" quer dizer recebe, ou seja, uma atribuição para uma variável.
#Toda variável (simples) é um espaço na memória (seria um espaço vetorial?)
#uma variável simples não consegue receber mais de uma definição (atribuição), pois se uma nova atribuição for
#designada para a variável simples que já possuia uma atribuição anterior, a nova atribuição vai substituir a primeira.
#As variáveis compostas permitem que uma mesma variável possua mais de uma definição (atribuição) ou consigam receber
#mais de uma definição (atribuição), sem que uma nova atribuição substitua uma atribuição anterior.
#As formas de criar uma variável composta é através das tuplas, listas e dicionários.

#Ao criar uma variável composta com n elementos, cada elemento vai ser representado por um número, sendo o primeiro
#elemento representado pelo número 0, o segundo pelp número 1 e assim por diante.
#exemplo dos lanches. lanche = hamburguer e lanche = suco... lanche[0] = hamburguer e lanche[1] = suco.
#uma string é uma variável composta. se eu tenho uma variável nome = rudá. o "r", "u", "d" e o "á" são pedaços de uma lista.
#ou seja, uma variável composta.
#voltando à variável lanche. se eu escrevo print(lanche)... será mostrado tudo, o hamburguer, o suco, a pizza e o pudim...
#porém, se eu escrevo print(lanche[2]), apenas a pizza será mostrada. da mesma forma que print(lanche[1]) só vai mostrar o suco.
#olhar a aula 9 - manipulando texto ou manipulando strings.
#também pode ser feito:
#print(lanche[0:2]) que vai mostrar o hamburguer e o suco e não a pizza, pois no fatiamento, o último elemento, nesse caso
#o 2(pizza), vai ser ignorado.
#print(lanche[1:]) vai mostrar o suco até o final (suco, pizza e pudim) pois não há nada depois dos ":"
#print(lanche[-1]) vai mostrar o pudim. [-2] vai mostrar a pizza e assim por diante, [-3] é o suco.
#outra função é o len(de length). assim o len(lanche) vai mostrar quantos elementos tem o lanche. len(lanche) = 4
#pode ser usada estrutura de repetições, assim:
#for c in lanche: (para cada comida em lanche, p/ c sendo comida)
#   print(c)
#como c não foi definido, o python vai criar um espaço na memória para a variável c (sendo ela uma variável simples)
#assim, para cada vez que o laço se repetir, o c vai receber uma nova comida do lanche. primeiro o hamburguer, depois o suco e assim por diante.
#quando o pudim (ultima variável de lanche) for mostrado, o laço terá fim e o programa seguirá.

#TUPLAS SÃO IMUTÁVEIS. depois que uma variável é definida dentro de uma tupla, ela não pode ser modificada. o python não permite.

#--------------------------------------------------------------------------------------------------------------------------

#AULA PRÁTICA

#No pyhton existe 3 maneiras de começar uma variável composta, usando: (), [] e {}. (depois do 3.5 não precisa mais disso)
#Onde os parênteses () são usados para as tuplas, os colchetes[] para as listas e as chaves{} para os dicionários.
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #tupla
print(lanche) #vai mostrar todos os lanches
print(lanche[1]) #vai mostrar somente o suco. P/ referenciar um dos itens em especifico, tem que usar o colchete...
print(lanche[-2]) #vai mostrar a Pizza
print(lanche[1:3]) #vai mostrar do elemento 1(suco) até o 3(pudim), mas o 3 é ignorado no fatiamento. ou seja, Suco e Pizza vai aparecer.
print(lanche[2:]) #vai mostrar do elemento 2 até o final. Pizza e Pudim
print(lanche[:2]) #vai mostrar do inicio até Pizza. porém a pizza é ignorada. ou seja, Hambúrguer e Suco.
print(lanche[-2:]) #vai começar na pizza e vai até o fim. Pizza e Pudim.
print(lanche[-3:]) #Suco, Pizza e Pudim.

print('-'*30)

#-----------------------------------------------
#TUPLAS SÃO IMUTÁVEIS

#lanche[1] = 'Refrigerante' . Ao fazer isso, o programa dá erro e não roda. "tuplas não suportam atribuições".
#print(lanche[1])

#-----------------------------------------------

for comida in lanche: #O laço vai repetir cada uma das comidas em ordem.
    print(f'Eu vou comer {comida}')  #O laço acaba após o print do pudim.
print('Comi pra caramba!!')

print('-'*30)

print(len(lanche)) #tamanho da tupla. quantos intens ela recebe.

print('-'*30)

for cont in range(0, len(lanche)): #vai começar a mostra a partir do item 0 até o total de itens da variável lanche (4).
    print(cont) #mas ao usar len(lanche) no for. o número 3(pudim) não será ignorado.
#print(cont) vai mostrar os números dos itens, ou seja, 0 1 2 3. mas ao fazer o for de outra maneira...
print('-'*30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}') #nesse caso, as comidas vão aparecer... Hambúrguer, Suco, Pizza e Pudim
print('Comi pra caramba!')

print('-'*30)
#ainda pode ser feito assim:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #como mostras os itens da tupla e sua posição
print('Comi pra caramba!')
print('-'*30)

for pos, comida in enumerate(lanche): #outra forma de mostrar os itens da tupla e sua posição
    print(f'Eu vou comer {comida} da posição {pos}')
print('Comi pra caramba!')
print('-'*30)

print(sorted(lanche)) #colocar em ordem alfabética
print('-'*30)

#criando novas tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c) #ele não soma, na verdade vai juntar as duas tuplas (2, 5, 4, 5, 8, 1, 2)
# ou seja, c=a+b(2, 5, 4, 5, 8, 1, 2) é diferente de c=b+a(5, 8, 1, 2, 2, 5, 4)
print(len(c)) #vai mostrar o tamanho da tupla... =7
print(c.count(5)) #quantas vezes está aparecendo o número 5 dentro da tupla c?? 2 vezes
print(c.index(8)) #vai mostrar em qual posição está o número 8 na tupla c: 4
print(c.index(2)) #vai mostrar em qual posição está o número 2 na tupla c: 0. ele pega a primeira aparição apenas.
print(c.index(2, 1)) #vai mostrar a posição do número 2 começando a procurar a partir da posição 1: 6

print('-'*30)
# A tupla em python é diferente de outras linguagens, ela aceita tanto número quanto nomes na mesma tupla. p/Ex:
pessoa = ('Rudá', 30, 'M', 80.00)
print(pessoa)
#A tupla é IMUTÁVEL, não se pode apagar um elemento apenas, por exemplo, mas é possível apagar a tupla toda usando o comando del.
#del(pessoa)
print('FINALMENTE FIM!! AMÉMMMM')
