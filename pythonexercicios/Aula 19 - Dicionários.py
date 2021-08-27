#AULA TEÓRICA - Listas (Parte 2)
#Dicionários são estruturas compostas como as tuplas e as listas, porém eles apresentam índices literais(escritos)
#Ao invés de tratar com números, posso dar nome aos componentes presentes numa lista ou tuplas (?)
#Os dicionários são identificados por chaves {}. desta forma, há duas formas de criar uma variável dicionário
#Se a variável for dados, para ser um dicionário tem que ser escrita de tais formas: dados = {} ou dados = dict()
#Assim, posso fazer...
#dados = dict()
#dados = {'nome':'Pedro', 'idade':25}
#Assim, ao invés de Pedro ser o índice 0, ele vai ser o índice nome, analogamente, 25 vai ser o índice idade ao invés de índice 1.
#Ou seja, não existe dados[0] e dados[1]. existe dados[nome] e dados[idade]
#Assim, se for feito um print(dados[nome]), vai aparecer 'Pedro', e print(dados[idade]) vai aparecer 25.
#Para adicionar elementos no dicionário, não se usa o comando .append... a forma correta de se adicionar é mais direta
#dados['sexo'] = 'M'. ou seja, se for feito um print(dados['sexo']) vai aparecer um 'M'
#Para remover um elemento de um dicionário, usa-se o comando del. deldados['idade']. Assim, o índice 'idade' será excluido
#O elemento e o valor são excluídos ao usar o comando del
#Outro exemplo seria criar uma variável filme, desta forma:
#filme = {
#
#        }
#Para criar um dicionário não importa se a segunda chave está na outra linha, mas que tenha duas chaves, uma abrindo e outra fechando
#Assim, posso fazer:
#filme = {'titulo':'Star Wars',
#         'ano':1977,
#         'diretor':'George Lucas'
#        }
#Nos dicionários existem nomenclaturas importantes chamadas valores, chaves e itens
#Ao fazer print(filme.values()), vai aparecer 'Star Wars', 1977, 'George Lucas', ou seja, os valores
#Ao fazer print(filme.keys()), vai aparecer 'titulo', 'ano', 'diretor', ou seja, as chaves
#Ao fazer print(filme.items()), vai aparecer tudo, tanto os valores quanto as chaves.
#Isso tem muita utilidade ao criar laços. Por exemplo
#for k, v in filme.items()                #p/ keys e values em filme.itens
#   print(f'O {k} é {v}')
#E vai aparecer, respectivamente: O titulo é Star Wars, O ano é 1977 e O diretor é George Lucas

#É possível juntar em um único programa as listas, tuplas e dicionários
#utilizando o exemplo acima, adicionando uma lista chamada locadora, é possível fazer:
#locadora = []
#filme = {'titulo':'Star Wars',
#         'ano':1977,
#         'diretor':'George Lucas'
#        }
#locadora.append(filme)
#Sendo o dicionario com os elementos do filme star wars o elemento 0 da lista locadora.
#Outros filmes poderiam ser adicionados como avengers e matrix
#Assim, ao fazer print(locadora[0]['ano']) vai aparecer 1977
#Da mesma forma que fazer print(locadora[0]['titulo']) vai aparecer 'Star Wars'

#---------------------------------------------------------------------------------------------------

#AULA PRÁTICA

pessoas = {'nome': 'Rudá', 'sexo': 'M', 'idade': 30}
print(pessoas) #Mostrar o dicionário pessoas
#print(pessoas[0])   #Dá erro, pois não é uma lista. pessoas[0] não existe.
print(pessoas['nome']) #Tem que colocar pessoas['nome'] pra mostrar o elemento 0. Rudá
print(pessoas['idade']) #Mostra a idade. 30
#O print formatado é feito de forma diferente
#print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')   #Feito desta forma está errado.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #Tem que usar aspas duplas pois a frase já está dentro de aspas simples.
print(pessoas.keys()) #Mostra as palavras chave do dicionário. 'nome', 'sexo', 'idade'
print(pessoas.values()) #Mostra os valores. 'Rudá', 'M', 30
print(pessoas.items()) #Mostra os items do dicionário. dict_items([('nome', 'Rudá'), ('sexo', 'M'), ('idade', 30)])
#Para este último, o python considera os items como uma lista composta por 3 tuplas.
print('-'*30)
#Também é possível acessar as chaves, os valores e os items por laços.
for k in pessoas.keys(): #Para toda key em pessoas.keys()
    print(k)  #Mostra as chaves
print('-'*30)
for v in pessoas.values(): #Mesma lógica das chaves
    print(v) #Mostra os valores
print('-'*30)
for k, v in pessoas.items(): #Para os items pode ser feito com duas variáveis para mostrar ambos formatados
    print(f'{k} = {v}')  #nome = Rudá, sexo = M, idade = 30
#O items serve como um substituto do .enumerate usado nas tuplas e nas listas.
print('-'*30)
#Agora vamos deletar o elemento(chave) sexo.
del pessoas['sexo']  #Comando para deletar um elemento do dicionário, nesse caso uma chave
for k, v in pessoas.items():
    print(f'{k} = {v}')  #nome = Rudá, idade = 30
print('-'*30)
pessoas2 = {'nome': 'Rudá', 'sexo': 'M', 'idade': 30}
pessoas2['nome'] = 'Leandro'  #Modificar o valor dentro da chave nome. Deixou de ser Rudá para ser leandro
for k, v in pessoas2.items():
    print(f'{k} = {v}') #nome = Leandro, sexo = M, idade = 30
print('-'*30)
#Para adicionar elementos também é simples:
pessoas2['peso'] = 98.5 #adicionando uma chave que não existia. a chave peso é adicionada de forma direta
for k, v in pessoas2.items():
    print(f'{k} = {v}') #nome = Leandro, sexo = M, idade = 30, peso = 98.5
print('-'*30)

#NOVO EXEMPLO - CRIAR UM DICIONÁRIO DENTRO DE UMA LISTA
brasil1 = []             #Lista chamada brasil que vai conter os dicionários dos estados
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} #Dicionário contendo informações do estado do Rio
estado2 = {'uf': 'Paraíba', 'sigla': 'PB'}     #Dicionário contendo informações da paraíba
brasil1.append(estado1) #Adiciona o dicionário estado1 na lista brasil
brasil1.append(estado2) #Adiciona o dicionário estado2 na lista brasil
print(brasil1) #Mostra a lista brasil contendo os dicionários estado1 e estado2
#Desta forma é possível mostrar prints como print(brasil[0]), one vai mostrar o Rio de janeiro
print(brasil1[0])
print(brasil1[1])
#Também pode ser feito assim:
print(brasil1[0]['uf']) #Vai mostrar Rio de Janeiro. o uf vai no lugar do que seria o [1], pois é um dicionário
print(brasil1[1]['sigla']) #PB

#NOVO EXEMPLO
estado = dict()   #Dicionário chamado estado
brasil = list()   #Lista chamada brasil
for c in range(0, 3): #Para cada contador no range de 0 a 3
    estado['uf'] = str(input('Unidade Federativa: ')) #Vai criar a chave 'uf' dentro do dicionário estado e fazer um input
    estado['sigla'] = str(input('Sigla do Estado: '))
#   brasil.append(estado[:]) #O comando [:] não é aceito para fazer cópias de dicionários em listas.
    brasil.append(estado.copy()) #Para copiar um dicionário em uma lista, usa-se o comando .copy()
print(brasil)
print('-'*30)
for e in brasil: #Para cada estado na lista brasil
    print(e) #Mostra cada estado como um dicionário
    for k, v in e.items(): #para cada key e value em items do estado
        print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()

#FIM