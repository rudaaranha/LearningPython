#AULA TEÓRICA - Funções (Parte 1)
#As funções em toda linguagem de programação estão ligadas à palavra rotina
#E a rotina seria algo que se faz constantemente e repetidamente
#Sendo assim, em python, muitas coisas são repetidas de forma constante... O QUE VOCÊ FAZ CONSTANTEMENTE??
#Até agora já usamos várias funções mesmo sem saber... a maioria funções que já vem com o python, como:
#print(), len(), input(), int(), float(), etc.
#Não há necessidade de determinar o que essas funções fazem. Elas já são pré definidas.
#Nem sempre essas funções satisfazem, por exemplo:
#Ao utilizar a linha de separação de resultado print('-'*30), tal linha é uma rotina.
#Sendo assim, é possível criar uma função para a linhas de separação.
#poderiamos chamá-la de mostralinha() por exemplo. Sendo ela uma rotina personalizada.
#(Pelo que eu entendi, tais funções funcionam como macros, forma de abreviar certos comandos)
#Essas rotinas personalizadas são as funções, ou def.
#A forma de fazer a função das linhas para que não precise fazer o print repetidamente seria:
#def mostralinha():
#   print('-'*30)
#ASSIM, um programa como ilustrado abaixo:
#print('--------------------------')
#print('    SISTEMA DE ALUNOS     ')
#print('--------------------------')
#print('--------------------------')
#print(' CADASTRO DE FUNCIONÁRIOS ')
#print('--------------------------')
#print('--------------------------')
#print('      ERRO DO SISTEMA     ')
#print('--------------------------')
#Pode ser refeito:
#def mostralinha():
#   print('--------------------------')
#mostralinha()
#print('    SISTEMA DE ALUNOS     ')
#mostralinha()
#mostralinha()
#print(' CADASTRO DE FUNCIONÁRIOS ')
#mostralinha()
#mostralinha()
#print('      ERRO DO SISTEMA     ')
#mostralinha()
#
#A utilização de parâmetros consegue potencializar o uso do def, por exemplo:
#No exemplo anterior a estrutura de linha, mensagem, linha se repete três vezes.
#É possível fazer uma def para que a estrutura se repita e só a mensagem seja modificada.
#def mensagem(msg):
#   print('--------------------------')
#   print(msg)
#   print('--------------------------')
#mensagem('SISTEMA DE ALUNOS'). #onde o sistema de alunos pode ser substituido depois por "CADASTRO DE FUNCIONÁRIOS"

#---------------------------------------------------------------------------------------------------

#AULA PRÁTICA

#ao invés de fazer:
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
def soma(a, b):
    s = a + b
    print(s)
    print('--------------')

#programa principal
soma(4, 5)
soma(8, 9)
soma(1, 2)
#se eu fizer soma(4), vai dar erro pois a variável soma recebe dois parâmetros
#também pode especificar quem é "a" e quem é "b"
soma(a=10, b=12)
#do mesmo jeito que
soma(b=10, a=12) #inverter a e b não influencia na execução do programa

#Aprimorando o exemplo anterior
def somaa(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-----------------')


#programa principal
somaa(a=4, b=5)
somaa(a=5, b=4)
#se foi deixar explicito quem é quem, a linguagem vai entender que o primeiro número é "a" e o segundo é "b"

#Empacotamento de parâmetros
#o empacotamento de parâmetros permite deixar em aberto o número de elementos de uma definição
#diferente do exemplo anterior que os elementos estavam bem definidos, eram 2 (A e B)
#com o empacotamente, eu posso colocar elementos variados. E a forma de fazer isso é:
#def contador(*num)  #o asterísco serve para deixar o número de elementos em aberto
#Exemplo abaixo

def contador(* num):
    print(num)


contador(2, 1, 7)        #vai aparecer (2, 1, 7). isso é uma tupla
contador(8, 0)           #vai aparecer (8, 0). outra tupla
contador(4, 4, 7, 6, 2)  #vai aparecer (4, 4, 7, 6, 2). mais uma tupla
#o resultado deste exemplo são a criação de 3 tuplas com os elementos do contador

def contadorr(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    print('--------------')


contadorr(2, 1, 7)
contadorr(8, 0)
contadorr(4, 4, 7, 6, 2)

# POR FIM, ainda é possível ao invés de fazer uma função def para uma tupla, ela pode ser usada para uma lista
#por exemplo, se eu tiver uma lista valores = [7, 2, 5, 0, 4] e preciso fazer com ela seja dobrada em alguns casos.
#a lista seria valores = [14, 4, 10, 0, 8]
#como se fosse uma dobra(valores), que não existe mas pode ser criada usando a função def

def dobra(lst):  #funcão criada para pegar valores de uma lista e multiplica-los por 2
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores) #lista valores
dobra(valores) #função criada para dobrar os elementos da lista valores
print(valores) #print da lista valores multiplicada por 2
print('---------------------------')

def somaaa(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')
    print('----------------------------')


somaaa(5, 2)
somaaa(2, 9, 4)
