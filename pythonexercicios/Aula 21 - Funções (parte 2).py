#AULA TEÓRICA - Funções (Parte 2)
#Tópicos a serem abordados na aula: Interactive help, docstrings, argumentos opcionais, escopo de variáveis e retorno de resultados.

#INTERACTIVE HELP
#É uma função interna do Python utilizada a partir do comando help()
#para utilizar o comando help() é só ir na parte Python console lá embaixo do programa. para sair é só digitar quit
#No Pyhton console e digitar help(). lá é possivel conseguir um manual de todas as funções do Python
#Como por exemplo: print, len, input, int, etc.
#pode ser usado para bibliotecas também, como: date, math, time, etc.
#Também é possível acessar a ajuda interativa de forma direta. escrevendo aqui help(print), por exemplo
#Ou pelo print, fazendo... print(input__doc__) para mostrar a funcionalidade do input

#-----------------------------------------------------------------------------------------------------------------------

#DOCSTRINGS
#É uma string de documentação... quando uso o comando help(input), ele me mostra a docstring do comando input
#Todas as funcionalidades internas do Python possui suas docstrings
#As docstrings servem também para acessar o manual de algum comando que não é uma função nativa do Python
#Ou seja, se eu crio uma função contador(i, f, p) usando a função def, é possível obter um manual desta
#funcão usando as docstrings, ou criar uma docstring que vai servir como manual da função def recém criada
#Para fazer uma função docstring, a pessoa deve adicioar 3 aspas duplas logo abaixo do def.
#EXEMPLO:
#-------------------------------------------------
#def contador(i, f, p):
#   """-> Faz uma contagem e mostra na tela.
#      :param i: inicio da contagem
#      :param f: fim da contagem
#      :param p: passo da contagem
#      :return: sem retorno
#   """
#   c = i
#   while c <= f:
#       print(f'{c}', end='')
#       c = c + p
#   print('FIM!')
#-------------------------------------------------
#
#Inclusive é possível criar uma docstring e colocar uma assinatura, como um direitos autorais
#
#-----------------------------------------------------------------------------------------------------------------------

#PARÂMETROS OPCIONAIS
#Parâmetros opcionais adaptam certas situações da função def, por exemplo:
#------------------------------
#def somar(a, b, c):
#   s = a + b + c
#   print(f'A soma vale {s}')
#------------------------------

#somar(3, 2, 5)   #Ao fazer isso, a função vai funcionar direitinho, somar 3 + 2 + 5= 10, pois a=3, b=2, e c=5
#Porém, ao fazer somar(8, 4), vai ocorrer um erro porque a=8, b=4, mas c não foi definido
#Para contornar o problema, pode-se usar os parâmetros opcionais, ao dar uma opcão caso,
#algum parâmetros não seja definido no uso da função, que seria o caso do exemplo somar(8, 4), onde o c não foi definido.
#Ficaria assim:
#------------------------------
#def somar(a=0, b=0, c=0)
#   s = a + b + c
#   print(f'A soma vale {s}')
#------------------------------
#desta forma, se por acaso algum parâmetro não for definido no uso da função, ele será igual a 0
#para o exemplo somar(8, 4), o c = 0 e a soma s = 12.
#Serve quando a pessoa não deseja utilizar os multiplos parâmetros (*num)

#-----------------------------------------------------------------------------------------------------------------------

#ESCOPO DE VARIÁVEIS
#Escopo em programação é o local onde uma variável vai existir e/ou o local onde uma variável não vai mais existir
#O primeiro exemplo é o de um escopo global
def teste():
    print(f'Na função teste, n vale {n}')


#programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
#ou seja, mesmo eu definindo um teste sem nada dentro e chamando de n, o pyhton reconhece uma variável n que recebe 2 mais a frente
#e quando teste() aparece no programa principal, n continua valendo 2
#porém, ao fazer o mesmo programa, mas adicionando uma variável x dentro da def teste, como mostrado abaixo:
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')


#programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}') #ao fazer esse print de x, o programa vai dar erro
#o erro ocorre porque a variável x foi definida apena na função teste() e não no programa principal, ou seja,
#essa variável não existe no escopo global, apenas no escopo local da função teste().
#já a variável n, diferente da x, é uma variável global, e vai funcionar tanto no programa principal, como na função local(teste)
#Se por acaso uma variável local n=5 for criada na função teste mesmo com a existência da variável global n=2
#ambas vão coexistir. porque ao fazer o print no programa principal, n=2, mas na função teste n=5 e ambas existem em seus domínios
#existe também uma forma de o 'a' local definido na def se tornar o a global do programa principal... segue abaixo
def testes(b):
    global a
    a = 8
    b = b + 4
    c = 2


a = 5
testes(a)
print(f'A fora vale {a}') #a vai ser igual a 8 e não igual a 5 pois o a de testes agora é o a global
#
#-----------------------------------------------------------------------------------------------------------------------

#RETORNANDO VALORES
def somar(a=0, b=0, c=0):
    print('-='*30)
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(2, 2)
somar(6)
#se eu faço a def somar assim, a resposta sempre vai ser a soma vale 10, a soma vale 4 e a soma vale 6
#mas e se eu quiser fazer, a soma vale 10, 6 e 4?
#Isso é possível com o comando return
#assim,
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s     #return s, pois s é minha vaiável


resp1 = soma(3, 2, 5) #como o return foi utilizado, a(s) resposta(s) de s vai(ão) estar em resp1. resp1 está diretamente ligada a return
#também pode ser feito com um print. print(soma(3, 2, 5))
#assim, pode ter mais de uma resposta, para que um print formatado possa existir, por exemplo resp2 e resp3, ou r1, r2 e r3
resp2 = soma(1, 7)
resp3 = soma(4)
print(f'Meus cálculos deram {resp1}, {resp2} e {resp3}.')

#---------------------------------------------------------------------------------------------------

#AULA PRÁTICA
def fatorial(num=1):
    print('-='*30)
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
#vamos executar de outra maneira
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
#Com o return também é possível retornar valores lógicos, verdadeiro ou falso, etc., e não apenas números
print('-='*30)


def par(n=0):
    print('-='*30)
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
