#AULA TEÓRICA - Listas (Parte 2)
#O conceito abordado nesta aula será o das listas dentro de outras listas
#Ao considerar uma estrutura(lista) chamada dados. dados = ['Pedro', 25]
#E gerar outra estrutura chamada pessoas. pessoas = list() ou pessoas = []
#É possível fazer o comando .append para adicionar elementos à lista pessoas.
#Também é possivel fazer o .append para lista pessoas puxando os dados de outra lista, neste caso a lista dados:
#pessoas.append(dados[:])
#Ao colocar os dois pontos entre os colchetes quer dizer que há um fatiamento completo da estrutura de dados da lista dados.
#Ou seja, foi feita uma cópia da lista dados para a lista pessoas. os dois pontos dentro dos colchetes serve para copiar elementos
#Na prática o que acontece é que na lista dados o elemento 0 (dados[0]) é 'Pedro' e o elemento 1(dados[1]) é 25.
#Já na lista pessoas, ao fazer o append da lista dados, o elemento 0(pessoas[0]) dela será a lista dados,
#Ou seja, o elemento 0 da lista pessoas(pessoas[0]) vai ser 'Pedro' e 25 e não apenas 'Pedro'.
#Além disso podem ser adicionados elementos de outras listas na lista pessoas, por exemplo:
#Se temos, dados2 = ['Maria', 19] e dados3 = ['João', 32], ao fazer...
#pessoas.append(dados2[:]) e pessoas.append(dados3[:]), a lista pessoas vai ter 3 elementos...
#O elemento 0(pessoas[0]) vai ser 'Pedro', 25; O elemento 1(pessoas[1]) vai ser 'Maria', 19;
#E o elemento 2(pessoas[2]) vai ser 'João', 32.
#A maneira que a lista pessoas vai ser representada em python (seja usando .append ou inserindo diretamente), vai ser:
#pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
#Assim, a lista pessoas vai conter outras 3 listas dentro de si, a dados, dados2 e dados3.
#Alguns comandos possíveis usando a lista pessoas seria:
#print(pessoas[0][0])  - mostra o elemento 0 da lista dados, uma vez que dados é o elemento 0 da lista pessoas. ou seja, 'Pedro'
#print(pessoas[1][1])  - mostra o elemento 1 da lista dados1, uma vez que dados1 é o elemento 1 da lista pessoas. ou seja, 19
#print(pessoas[2][0])  - mostra o elemento 0 da lista dados2, uma vez que dados2 é o elemento 2 da lista pessoas, ou seja 'João'
#No print(pessoas[0][0]), o primeiro [0] faz referêcia ao elemento 0 da lista pessoas e o segundo [0] faz refência ao elemento 0
#da lista interna, ou seja, o elemento 0 da lista dados.
#para dar nomes ao elementos, por exemplo, fazer o segundo [0] ser referente a pessoas e o segundo [1] ser referente a idade,
#tem que usar os dicionários, aula 19.
#Se for feito um print(pessoas[1]), como o elemento não foi especificado, a lista inteira vai ser mostrada. ['Maria', 19]

#---------------------------------------------------------------------------------------------------

#AULA PRÁTICA
teste = list() #criação de uma lista teste
teste.append('Rudá') #adicionando o primeiro elemento da lista teste
teste.append(30) #adicionando o segundo elemento da lista teste
galera = list()  #criação de uma segunda lista chamada galera
#galera.append(teste) #adicionando a lista teste na lista galera, porém cria-se um link, o certo é fazer como mostrado na linha abaixo
galera.append(teste[:])  #comando usado para copiar a lista teste sem formar o link
print(galera)
print('-'*30)
teste[0] = 'Maria' #mudando o elemento 0 da lista teste que era 'Rudá' e agora é 'Maria'
teste[1] = 22      #mudando o elemento 1 da lista teste que era 30 e agora é 22
#galera.append(teste[:])  #o link seria criado junto com o anterior e ao dar print, seria mostrado como na linha abaixo
#print(galera)     #nesse caso criou-se um link entre as duas listas por isso o print foi [['Maria', 22], ['Maria', 22]]
# o certo seria usar galera.append(teste[:]) para apenas copiar a lista teste.
galera.append(teste[:]) #ao apenas copiar, o ['Rudá', 30] adicionado à lista anteriormente é mantido e é adicionado o ['Maria', 22]
print(galera)          #[['Rudá, 30'], ['Maria', 22]]

print('-'*30)

#fazendo outro exemplo
galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] #lista galera1 com 4 estruturas compostas dentro de outra estrutura
print(galera1)       #vai motrar a lista toda
print(galera1[0])    #vai mostrar os dados do joão. ['João', 19]
print(galera1[0][0])  #vai mostrar apenas o 'João'
print(galera1[2][1])  #vai mostrar apenas o 13. [2] são os dados do joaquim e o [1] é a idade dele
print('-'*30)
for p in galera1:     #para cada pessoa em galera, print(galera)
    print(p)          #serão printados todos os elementos de galera1, um abaixo do outro. ['João', 19] depois ['Ana', 33], etc.
print('-'*30)
for p in galera1:
    print(p[0])       #só os nomes de galera1
print('-'*30)
for p in galera1:
    print(p[1])       #só as idades de galera1
print('-'*30)
for p in galera1:
    print(f'{p[0]} tem {p[1]} anos de idade.') #vai mostrar o print formatado dos nomes e idades

print('-'*30)
#Fazendo outro exemplo
galera2 = list()       #criando a lista galera2
dado = list()         #criando a lista dado
for c in range(0, 3):    #para um contador de 0 até 3
    dado.append(str(input('Nome: '))) #serão adicionados 3 elementos(nomes) à lista dado, nesse caso elementos pares [0, 2, 4]
    dado.append(int(input('Idade: '))) #serão adicionados 3 elementos(idades) à lista dado, nesse caso elementos ímpares [1, 3, 5]
    galera2.append(dado[:]) #ao fazer isso, o primeiro nome e a primeira idade serão o elemento 0 da lista galera2,
    # o segundo nome e a segunda idade serão o elemento 1 da lista galera2 e assim por diante. como uma cópia
    dado.clear() #Comando para limpar a lista dado. Porém, no print(galera2) tudo será reproduzido sem problemas, pois foi feita uma cópia
    #Se por acaso se a pessoa esquecer do [:] no append da galera2. tudo da galera será apagado também(vai aparecer colchetes vazios),
    #pois dado e galera2 estarão linkados
print(galera2)
print('-'*30)
totmaior = totmenor = 0
for p in galera2: #para cada pessoa em galera2
    if p[1] >= 21:  #se a idade p[1] foi maior ou igual a 21
        print(f'{p[0]} é maior de idade.') #o nome p[0] é maior de idade
        totmaior = totmaior + 1 #o total maior de idade é zero e vai ser somado mais toda vez que a condição for atendida
    else:
        print(f'{p[0]} é menor de idade.') #o nome p[0] é menor de idade
        totmenor = totmenor + 1  #o total menor de idade é zero e vai ser somado mais toda vez que a condição for atendida
print(f'Temos {totmaior} maior(es) e {totmenor} menor(es) de idade.')
print('FIM')
