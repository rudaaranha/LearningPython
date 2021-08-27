#Ex064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
#o valor qqq, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
#(Desconsiderando o flag).
n = cont = soma = 0 #pode colocar todas as variáveis na mesma linha
n = int(input('Digite um número [999 para parar]:')) #ao colocar a pergunta fora e dentro, o flag não conta para as somas do laço
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e sua soma foi igual a {}.'.format(cont, soma))

#Ao colocar a variável depois da soma e da cont ao digitar 999, não haverá problema pois 999 é o comando de parada, ou seja,
# vai direto para o último print sem realizar o laço de soma e cont.