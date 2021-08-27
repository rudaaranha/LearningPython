#AULA TEÓRICA - Listas (Parte 1)

#Começamos dizendo que tuplas são imutáveis. uma vez que uma variável é definida, a mesma não pode ser modificada
#posteriormente. Porém tem como fazer esse tipo de modificação em python. Seria usando outra variável composta: as listas

#Para identificas as listas, usa-se colchetes[]. As tuplas usam parenteses()
#O exemplo da aula passada seria lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
#Assim, se posteriormente for feito Lanche[3] = 'Picolé'. O pudim vai ser substituido pelo picolé, pois as listas são mutáveis

#Porém, não é possível adicionar novos elementos de forma direta. ou seja, não posso fazer:
#lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] e depois fazer lanche[4] = 'Café'. pois lanche[4] não existe
#Mas há um comando que permite adicionar novos elementos à lista. Assim, se eu uso o comando ".append", o "café" pode ser adicionado
#Assim, para adicionar o "café" teria que fazer lanche.append('Café'). O comando append adiciona um elemento ao final da lista

#Para adicionar algum elemento entre os outros elementos existentes ou mesmo no inicio da lista, existe outro comando: ".insert"
#Assim, para adicionar "cachorro quente" teria que fazer um lanche.insert(0,'Cachorro quente'). onde o número zero indica a posição
#onde o novo elemento será adicionado. e os outro elementos que já existiam ficam uma posição à frente

#Também é possível apagar elementos da lista. Na tupla não era possível, apenas apagando a tupla toda
#O comando mais básico é o "del". assim, seria possível fazer um dellanche[3] para eliminar a pizza
#Outro método é o ".pop". lanche.pop(3). normalmente o pop é feito para eliminar o último elemento com o lanche.pop()
#Ainda pode usar o ".remove", mas no remove a pessoa indica o elemento e não sua posição
#assim, para eliminar a pizza poderia ser feito com lanche.remove('Pizza')
#Ao eliminar qualquer elemento, independente do método, o python vai reorganizar os demais elementos automáticamente.
#Ao tentar eliminar um elemento que não existe, o programa dá erro. mas uma forma de evitar o erro e conferir se o elemento existe
#é utilizando o comando if. por exemplo if 'pizza'in lanche: lanche.remove('Pizza'). COMANDO SUPER IMPORTANTE

#é possivel usar um comando para declarar uma lista. assim, é possivel fazer: valores = list(range(4, 11)). começa em 4 e para em 10.
#valores = list(range(4, 11)) é a mesma coisa que valores = [4, 5, 6, 7, 8, 9, 10]

#Se temos uma variável valores = [8, 2, 5, 4, 9, 3, 0] e queremos deixá-la em ordem, podemos usar o comando ".sort()"
#Assim, valores.sort() vai deixar a variável valores ordenada: valores = [0, 2, 3, 4, 5, 8, 9]. imagino que sirva para palavras também.
#para deixar na ordem invertida, ou seja, valores = [9, 8, 5, 4, 3, 2, 0] também existe como usando o comando ".sort"
#seria o valores.sort(reverse=True)
#len(valores) vai mostrar o tamanho da lista. Ou seja, 7 elementos. Muito útil na hora de fazer algum laço

#---------------------------------------------------------------------------------------------------

#AULA PRÁTICA

num = [2, 5, 9, 1] #lista criada
print(num)
num[2] = 3 #diferente das tuplas, nas listas é possível modificar uma variável previamente determinada
print(num) #o print da nova variável num vai ser [2, 5, 3, 1]
num.append(7) #ao fazer isso, uma nova atribuição é criada para a variável num. num = [2, 5, 3, 1, 7].
#uma nova atribuição não pode ser adicionada de forma direta, ou seja, num[4] = 7. tem que usar o comando append
print(num)
num.sort() #forma de deixar a lista em ordem, nesse caso crescente. [1, 2, 3, 5, 7]
print(num)
num.sort(reverse=True) #lista em ordem decrescente. [7, 5, 3, 2, 1]
print(num)
print(f'Essa lista tem {len(num)} elementos.') #mostrar a quantidade de elementos da lista. 5 elementos
num.insert(2, 0) #comando usado para adicionar o elemento 0(zero) na posição 2 da lista.
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(6, 4) #também é possível adicionar elementos em uma posição que anteriormente não existia (posição 6)
print(num) #Mesmo se essa posição fosse muito acima. por exemplo, para essa lista, eu tivesse colocado a posição 15.
print(f'Essa lista tem {len(num)} elementos.')
print('------Eliminação de elementos------')
num.pop() #remover o último elemento da lista. [7, 5, 0, 3, 2, 1]
print(num)
num.pop(5) #remover o elemento na posição 5. [7, 5, 0, 3, 2]
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop(2) #remover o elemento na posicão 2. [7, 5, 3, 2]
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0) #adicionar o elemento 0 na posição 2. [7, 5, 0, 3, 2]
num.insert(5, 1) #adicionar o elemento 1 na posição 5. [7, 5, 0, 3, 2, 1]
print(num)
num.insert(2,2) #adicioanar o elemento 2 na posição 2. O elemento zero agora fica posicionado na posição 3. [7, 5, 2, 0, 3, 2, 1]
print(num)
num.remove(2) #remover o elemento 2 (o número). o python procura a primeira ocorrência do elemento e a elimina. [7, 5, 0, 3, 2, 1]
print(num) #a eleiminação de elementos também pode ser feito através dos laços.
#É o caso de colocar pra remover algum elemento que não existe na lista (ocorre erro no programa).
# P.Ex: num.remove(4). o número 4 não está na lista. porém... ao usar um laço, o erro pode ser evitado
print('-'*30)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num) #o número 4 não está no programa, mas ele funciona sem problemas por causa do laço.
num.insert(10, 4) #agora vamos adicionar o número 4. [7, 5, 0, 3, 2, 1, 4]
print(num)
if 4 in num: #e caso tenha o número 4, ele será removido da lista.
    num.remove(4)
print(num) #[7, 5, 0, 3, 2, 1].

print('-'*30)
print('NOVO EXEMPLO')
print('-'*30)

#Começar criando uma lista vazia chamada valores. tem duas maneiras de fazer: valores = [] ou valores = list()
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...', end='') #mostrar os valores de outra maneira
print('')
for c, v in enumerate(valores): #pegar tanto as chaves quantos os valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('-'*30)
Valores = list() #criando outra variável Valores, agora com V maiúsculo para não dar problemas no programa
for cont in range(0, 5): #ler valores pelo teclado e ir adicionando à lista.
    Valores.append(int(input('Digite um valor: '))) #usando o comando append para fazer um imput.
    #Ou seja, como o range é de 0 a 5, 5 número terão que ser digitados por causa do for.
for c, v in enumerate(Valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-'*30)
print('NOVO EXEMPLO')
print('-'*30)

#se eu determino uma lista "a" e faço uma váriável "b" igual a "a". ele vai mostrar "b" como sendo a lista "a".
a = [2, 3, 4, 7]
b = a
print(f'A lista A: {a}')
print(f'A lista B: {b}')
# caso eu mude algum valor na lista "b"... tipo b[2] = 8, a lista "a" também será modificada.
b[2] = 8
print('-'*10)
print(f'A lista A: {a}')
print(f'A lista B: {b}') #o python não apenas copia uma lista em outra, mas faz uma ligação entre elas.
#para copiar uma lista em outra apenas, deve ser feito d = c[:]. aula de fatiamento (novas variáveis pra não dar problema)
c = [2, 3, 4, 7, 1]
d = c[:]
print('-'*10)
print(f'A lista C: {c}')
print(f'A lista D: {d}')
#Agora modificando apenas a lista d... d[2] = 8
print('-'*10)
d[2] = 8
print('-'*10)
print(f'A lista C: {c}')
print(f'A lista D: {d}')
print('FIM')
