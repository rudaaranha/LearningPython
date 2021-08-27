#AULA TEÓRICA - Tratamento de erros e exceções
#Essa aula serve para saber arranjar soluções para eventuais erros na execução dos programas.
#Além de aprender a ler um erro. como identificá-lo e eventualmente sulucioná-lo.

#Por exemplo, ao fazer print(x) e não definir a variável x, o programa vai dar erro.
#print(x) #ao mandar rodar, vai ocorrer uma erro mostrado em vermelho. indicando a linha(5) e o tipo de erro.

#nesse caso "NameError: name 'x' is note defined. x não foi definido.
#Quando esse tipo de erro não ocorre de forma sintática, ou seja, o comando foi escrito de forma correta,
#O erro é chamado de exceção. A exceção do exemplo chama-se NameError.

#Outro exemplo de erro seria em um código do tipo:
#n = int(input('Número: ')) #código perfeitamente digitado
#print(n) #aqui também

#Do jeito que está o exemplo funciona perfeitamente, a não ser em casos de EXCEÇÃO onde um número inteiro não é digitado
#ao escrever oito ao invés de 8, o programa vai dar erro.
#Nesse caso um erro de valor: "ValueError: invalid literal for int() with base 10: 'oito'
#O erro ocorre porque a palavra 'oito' não pode ser convertida para inteiro pela função int.
#Assim, uma forma de tentar corrigir ou contornar os erros do programa é identificar suas exceções.
#E se não conhecer qual exceção ocorreu, é só pesquisar pra entender e tentar corrigir (papai google).

#Outra forma de identificar erros é utilizando o comando 'try' e depois o comando 'except'
#A forma de funcionamento seria de tente alguma coisa(try) senão uma exceção(except)
#dentro do try devem ser colocados os comandos que podem dar problemas
#e no except colocar as falhas(se eu tentar e falhar, o que vai acontecer?)
#E se der certo, o else pode ser usado como dando o resultado correto do programa.
#Por fim pode ser usado o 'finally'. o finally vai ocorrer independente se deu certo ou se deu erro.
#lembrando que else e finally são opcionais, podem ou não ser usadas

#--------------------------------------------------------------------------------------------
#AULA PRÁTICA
#Na aula prática será feito um exemplo usando o try como forma de resolver um possível erro sem que a mensagem de erro seja recebida
#O mesmo try pode ter vários exceptions como forma de dar tratamento aos diferentes tipos de erros para o mesmo código.

try:      #Ao invés de mandar fazer isso tudo, podemos mandar o Python tentar rodar esse código.
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b    #vai ocorrer erro se o valor de b = 0.
except Exception as erro: #Primeiro modo de tratar o erro. única forma de conseguir formatar a frase mostrando o erro
    print('Infelizmente tivemos um problema... =(') #O except pode ser usado para mostrar o erro que ocorreu usando o Exception as erro
    print(f'O problema encontrado foi {erro.__class__}.') #O interessante de usar essa ferramenta é quando estiver desenvolvendo o código.
except (ValueError, TypeError): #segundo modo de tratar o erro. Personalizar uma frase para um determinado tipo de erro
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!') #Personalizar uma frase para um determinado tipo de erro
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:         #Ao utilizar o else, o erro em vermelho para de aparecer. Isso é conhecido como tratamento de erro
    print(f'O resultado é {r:.2f}.')
finally:
    print('Volte sempre! Muito obrigado!')

#duvida: o try deve ser usado em programas que rodam, pois o não aparecimento do erro pode comprometer o entendimento de possíveis erros?

#FIM