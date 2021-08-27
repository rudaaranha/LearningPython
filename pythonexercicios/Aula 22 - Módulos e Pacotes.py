#AULA TEÓRICA - Módulos e Pacotes
#Modularização é o ato de construir módulos. Tendo surgido no início da década de 60.
#Uma vez que os programa foram ficando muito extensos, surgiu a necessidade compactar ou seperar em módulos tais programas.
#Facilitando o entendimento, manutenção e processamento de tais programas.
#Sendo assim, a modularização vai dividir programas grandes. separando-os em pequenos módulos
#Melhorar a legilibilidade. Os módulos vão conter pequenas partes do programa, facilitando a busca por determinada parte do mesmo.
#A manutenção se torna mais simples pois pode ser feita de módulo em módulo e não no programa de uma vez.


#tendo um primeiro exemplo a utilização de fatorial dentro de um programa:
#def fatorial(n):
#   f = 1
#   for c in range(1, n+1):
#       f = f * c
#   return f


#def dobro(n):
#    return n * 2


#def triplo(n):
#    return n * 3 #as funções estão como mensagem para fazer o módulo funcionar
#Concorda que o programa vai ficar grande quando as funções forem adicionadas?
#Imagine adicionar mais 10 funções com a ferramenta def.
#Algo que pode ser feito é usar a modularização. Onde em um módulo vão estar todas as funções usadas.
#E no outro módulo vai estar o programa principal.
#Assim, um arquivo será criado(nesse caso, chamado de uteis.py), e todas as funções do programa serão adicionadas neste arquivo.

#Assim sendo, o arquivo uteis.py é um módulo do meu projeto.
#O módulo criado funciona igual aos módulos já existentes, como time e math, onde é possível importar
#Em python, qualquer arquivo .py pode ser um módulo
#A forma de ligar os módulos no programa é dando import no módulo criado:
import aula22uteis


#programa principal
num = int(input('Digite um valor: '))
#fat = fatorial(num) #antes de usar o módulo
fat = aula22uteis.fatorial(num)    #forma correta de usar o módulo. embora já tenha sido importado, eu tenho que especificar o que eu quero do módulo
print(f'O fatorial de {num} é {fat}.')
#print(f'O dobro de {num} é {dobro(num)}.') #antes de usar o módulo
print(f'O dobro de {num} é {aula22uteis.dobro(num)}.')
#print(f'O triplo de {num} é {triplo(num)}.') #antes de usar o módulo
print(f'O triplo de {num} é {aula22uteis.triplo(num)}.')

#Uma forma de não precisar especificar o que eu preciso no módulo (aula22uteis.fatorial, aula22uteis.dobro) é fazer o from import
#se eu faço from aula22uteis import fatorial, dobro, triplo. eu não preciso especificar no print.
#o mais indicado para programas grandes é importar o módulo completo e não partes dele para não criar conflitos.

#Vantagens de usar a modularização
#- Organização do código
#- Facilidade de manutenção
#- Ocultação de código detalhado. Eu não preciso saber como calcula o fatorial, mas que a função fatorial faz isso pra mim
#- É possível reutilizar os módulos em outros projetos sem que seja preciso refazer tudo.


#-------------------------------------------------------------------------------------------------------------------
#AULA PRÁTICA

#E quando os módulos ficarem muito grandes para serem importados de um por um, a solução é a utilização dos pacotes
#Os pacotes nada mais são que a junção dos módulos. Estes últimos podendo ser separados por assunto.
#Ao invés de ter um módulo chamado de úteis, agora é possível ter um pacote chamado de úteis.
#E dentro desse pacote ter vários módulos separados para tratamento de:
#números, strings, datas, cores, etc.
#E a importação do pacote uteis é feita do mesmo jeito do módulo: import uteis.
#como também podem ser feitas importações específicas dentro dos pacotes: from uteis import datas.
#Lembrando que qualquer arquivo .py pode ser um módulo. analogamente, toda pasta é considerada um pacote.
#Assim, o modo mais fácil de criar um pacote em python é através de pastas.
#assim, eu posso criar uma pasta com nome uteis...
#E dentro de cada pasta, posso criar outras pastas com o nome de cores, data, números e strings.
#dentro de cada pasta criada (cores, datas, etc)  tem que ter uma arquivo chamado __init__.py
#Para criar o pacote, ao invés de ir em python file, dentro da pasta do projeto, a pessoa vai em python package.
#E o código anteriormente criado pode ser jogado na pasta números (mais especificamente no arquivo __init__.py)
#e para importar um módulo dentro de um pacote seria from uteis import números (uteis é o pacote e numeros é o módulo)
#o print ficaria: print(f'O dobro de {num} é {numeros.dobro(num)}')   Usando a mesma função feita anteriormente

#FIM
