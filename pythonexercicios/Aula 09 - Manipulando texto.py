#Testes iniciais
#Ao utilizar frase[x:y:z] x é a str inicial, y é a str final e z é o passo entre as str (ex frase[3:15:2] str 3 até a str 15 pulando de 2 em 2)
#Quando quiser escrever textos longos, não precisa dar print em linha por linha, pode-se utulizar de '''(tres aspas)(Ex '''texto''')
#Ele entende a utilização do ponto. ex print(frase.count('o')) - ele vai contar quantas letras o existe em frase. 'o' minúsculo é diferente de 'O' maiúsculo
#Mas se usar o print(frase.upper().count('O')). transforma tudo em maiúsculo e conta quantos "O"s aparecem
#A função "len" mostra o tamanho da frase. Os espaços são cotados, ou seja, 'Curso em vídeo python' é menor que '    Curso em vídeo python   '.
#Ao se utilizar a função strip, os espaços excedentes são removidos. ex print(len(frase.strip())), assim a frase '    Curso em vídeo python    ' tem 21 caracteres.
#A função replace troca uma frase por outra. ex python por android
#as str são imutáveis. o replace não consegue modificar a natureza da frase. por ex:
#frase='Curso em Vídeo Python'
#frase.raplace('Python', 'Android')
#print(frase)
# a frase não será modificada pois ela é imutável. vai aparecer 'Curso em Vídeos Python'. Para modificar teria que fazer na segunda linha frase=frase.replace('Python', 'Android')
#lembrar que letras maiúsculas e minúsculas fazem diferença pra linguagem
#A função split() divide uma frase pelos espaços dela

frase='Curso em Vídeo Python'
print(frase[3]) #frase[3] é a quarta letra. o número 3 indica o quarto caractere da frase, lembrando que começa no número zero. os espaços também contam
print('-'*130)


frase='Curso em Vídeo Python'
print(frase[3:13]) #Agora fazendo o fatiamento entre os caracteres 3 e 13 (da letra "s", até a numero 12 "e") fica "so em Víde". O ultimo número do fatiamento não aparece...
print('-'*130) #O 13 que seria "o" de Vídeo.


frase='Curso em Vídeo Python'
print(frase[:13])#Fazendo fatiamento do inicio até o caractere 13 (lembrando que o caractere 13 não aparece), ou seja, de 0 até 13. "Curso em Víde"
print('-'*130)


frase='Curso em Vídeo Python'
print(frase[13:]) #Fazendo fatiamento do caractere 13 até o final. "o Python"
print('-'*130)


frase='Curso em Vídeo Python'
print(frase[1:15:2]) #Fatiamento do caractere 1 até o 15 (o 15 não aparece), saltando de 2 em 2. "us mVdo"
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.count('o')) #Conta quantas vezes aparece a letra "o" (o minúsculo pois tem diferença pro python)
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.upper().count('O')) #coloca toda a frase em maiúsculas (.upper()) e conta quantas vezes aparece a letra "O"(nesse caso o maiúsculo já que a frase está toda em maiúsculas)
print('-'*130)


frase='Curso em Vídeo Python'
print(len(frase)) #vê qual o tamanho da frase (número de caracteres). nesse caso "Curso em Vídeo Python" tem 21 caracteres.
print('-'*130)


frase='    Curso em Vídeo Python    '
print(len(frase)) #ao adicionar espaços antes e depois das letras, o número de caracteres também aumenta. A frase passa a ter 29 caracteres.
print('-'*130)


frase='    Curso em Vídeo Python    '
print(len(frase.strip())) #A função .strip() remove os espaços indesejáveis (colocados antes e depois da frase)
print('-'*130)


frase='Curso em Vídeo Python'
frase.replace('Python', 'Android') #O replace substitui uma palavra por outra na frase. nesse caso foi substituido Pyhton por Android. Porém, sem uma função o python não reconhece.
#nesse caso, ainda vai aparecer "Curso em Vídeo Python"
print(frase) #Uma string é imutável a não ser que uma função de transformação de string seja utilizada para realizar uma atribuição, nesse caso foi o replace(substituição)
print('-'*130)


frase='Curso em Vídeo Python'
frase=(frase.replace('Python', 'Android'))#Já nesse caso uma função foi utilizada: frase = frase.replace('Python', 'Android'). desta forma, a substituição ocorre.
print(frase)
print('-'*130)


frase='Curso em Vídeo Python'
print('Vídeo' in frase) #verifica se a palavra vídeo existe na frase (lembrado que frase é a váriável, poderia ser palavra) a resposta dada é True
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.find('Vídeo')) #procura pela palavra Vídeo e diz a posição que ela começa. nesse caso "Vídeo" começa na posição 9.
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.find('vídeo'))#vídeo com v minúsculo não existe na frase. A resposta dada pelo programa é -1
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.lower().find('vídeo'))#Mas ao transformar toda a frase em minúsculas ".lower()" e procurar por "vídeo" ele vai responder que está na posição 9.
print('-'*130)


frase='Curso em Vídeo Python'
print(frase.split())
#A função split() divide a frase. vai aparecer algo como ['Curso', 'em', 'Vídeo', 'Python'] - sendo a resposta uma lista com as palavras que compõe a frase
#listas em pyhton são identificadas por colchetes.
#nesse exemplo foi criada uma lista com separador de espaços
print('-'*130)


frase='Curso em Vídeo Python'
dividido=frase.split()#nesse caso a variável dividido vai receber a frase de forma dividida, criando uma lista como já foi feito com as palavras que compõe a frase.
print(dividido[0]) #Porém, ao fazer "print('dividido[0]), ele vai mostrar só a palavra Curso, pois na lista criada "['Curso', 'em', 'Vídeo', 'Python']", Curso é a palavra 0
#Da mesma forma que "em"-1, "Vídeo"-2 e "Python"-3.


print('-'*130)
frase='Curso em Vídeo Python'
dividido=frase.split()
print(dividido[2][3]) #nesse caso ele vai pegar a terceira letra da palavra dois, ou seja, a letra 'e' da palavra 'Vídeo'. A letra 'V' é 0(zero)
