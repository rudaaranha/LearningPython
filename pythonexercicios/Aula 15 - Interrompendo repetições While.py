#AULA TEÓRICA - Laços de repetição parte 3
#Nesta aula aprenderemos um comando para interromper um laço (nesse caso um while já que o for é pré-definido).
#Existem 3 laços de repetições na programação (While, For e Repeat), porém em python só existem duas (While e For).
#Nesse método, o while não tem condição para sair do laço, ou seja, ele teoricamente fica repetindo eternamente.
#assim, outro comando é adicionado ao laço inicial, uma parada (usada para interromper o laço), que leva diretamente
# ao fim do laço quando certas condições são atendidas.
#Assim, a forma correta de escrever o exemplo da maçã seria (interessante que nesse caso não existe maçã kkk):
#while true:            (O laço while true é chamado de laço infinito pois não tem condição de saída do laço pré-definida)
#   if 'tiver chão na frente':
#       passo
#   if 'tiver buraco':
#       pula
#   if 'tiver moeda':
#       pega
#   if 'tiver troféu':
#       pega
#       break           (Comando para interromper o laço)

#-----------------------------------------------------------------------------------------------------

#AULA PRÁTICA
#Repetindo um exercício de contagem da aula passada...
#cont = 1
#while cont <= 10:
#   print(cont, '-> ', end='')
#   cont += 1
#print('Acabou')

#----------------------------------------------------------------
#programa que determina uma quantidade de número a ser lido a partir de um contador
n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1

#Porém, se quantidade de números não for pré determinada? Se não quiser trabalhar com o contador?
n = 0
while n != 999:
    n = int(input('Digite um número: ')) #assim o programa vai ler número infinitamente até que o número 999 for digitado.
#O 999 é o flag, ou seja, o ponto de parada

#E se por acaso eu quiser somar os números que forem digitados?
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s = s + n
s = s - 999 #Como o ponto de parada é 999, ele não deve entrar na soma, por isso a subtração (sendo ela um gambiarra)
print('A soma vale {}.'.format(s))

#Para que a gambiarra não seja necessária, o comando break deve ser utilizado
n = s = 0           #O ponto inicial continua sendo necessário\
while True:         #comando de laço infinito necessário para utilização do comando break (?)
    n = int(input('Digite um número: '))
    if n == 999:    #ao invés de colocar a condição de parada no laço (if  e depois break), ele é adicionado como uma condição interna
        break       #desta forma o laço fica ativo infinitamente até que a condição seja satisfeita devido ao break
    s = s + n       #Ao adicionar a soma fora da condição (if), o número 999 (condição de parada do laço), não entra na soma
#print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.') #Utilizando fstring, uma forma mais simples de formatar uma string (sem a necessidade do .format)