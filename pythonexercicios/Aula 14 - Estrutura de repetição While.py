#AULA TEÓRICA
#É uma estrutura de repetição mais complexa, Utilizada quando a repetição 'for' não conseguir satisfazer as necessidades.
# Estrutura de repetição com teste lógico.
#Quando a pessoa não sabe a quantidade de repetições necessárias. Por exemplo, no 'for', o range determina o inicio e o fim da repetição.
#No while não existe o range.
#A forma certa de escrever seria:
#while not maçã:                       - acredito que maçã seja uma variável(?)
#   passo                             - o que será repetido até concluir a variável.
#pega
#while em tradução literal significa enquanto. 'not' é não... ou seja, enquanto não maçã (enquanto não tiver na maçã, ou enquanto não tiver maçã) aula 14.
#aula 14: boneco pulando bloco, pegando moeda e depois a maçã
#while not maça:
#   if 'tiver chão na frente':
#       passo
#   if 'tiver buraco':
#       pular
#   if 'tiver moeda':
#       pegue
#pega

#-----------------------------------------------------------------------------------------------------

#AULA PRÁTICA
#exemplo 1 - terá equivalente para o for
c = 1 #c começa com 1.              --------------------------------- equivalente em for:
while c < 10: #enquanto c(contador) for menor que 10.  -------------- for c in range (1, 10):
    print(c)                                 #-----------------------   print(c)
    c = c + 1 #ou c =+ 1 (necessário porque a cada volta que ele dá, o contador(c) é somado mais 1)
print('Fim')                                 #----------------------- print('fim)

print('-' * 60)
#for c in range(1, 5):
#   n = int(input('Digite um valor:'))
#print('Fim')
#vamos considerar um programa que só vai parar quando o valor zero(0) for digitado.
n = 1 #Aparentemente sempre há a necessidade de determinar o inicio do contador (n=1). seria o inicio do range, fazendo uma analogia ao for.
while n != 0: #enquanto o número for diferente de zero. Esse é o chamado ponto de condição de parada.
    n = int(input('Digite um valor:'))
print('Fim') #quando a condição é atendida, ou seja, o número zero foi digitado.

print('-' * 60)
r = 'S' #A condição sempre tem que ser determinada.
while r == 'S': #enquanto r for igual a S(sim). equanto a resposta for sim, a pergunta será repetida.
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

print('-' * 60)

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1 #par = par + 1
        else:
            impar += 1 #impar = impar + 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
