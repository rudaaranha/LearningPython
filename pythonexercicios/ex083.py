#Ex083 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao: #para qualquer simbolo na expressão
    if simbolo == '(':   #se o simbolo for igual a "("
        pilha.append('(') #adicionar o simbolo "(" na lista pilha.
    elif simbolo == ')':  #se o simbolo for igual a ")"
        if len(pilha) > 0: #se o tamanho da pilha for maior que zero, ou seja, a lista pilha tem algum elemento dentro.
            pilha.pop()  #vai remover o último elemento da lista pilha
        else: #se não tiver nenhum elemento na lista pilha
            pilha.append(')') #adicionar um elemento ")"na lista pilha. para o caso de esquecer de colocar o parêntese abrindo
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão matemática não é valida!')
#sempre que o programa identificar um parêntese abrindo"(", este é adicionado na pilha.
#sempre que o programa identificar um parêntese fechando")", um parêntese abrindo é retirado da pilha pois encontrou seu par.
#Assim, quando a lista estiver vazia, quer dizer que todos os pares estão certinhos.
#Se a lista tiver algum elemento, quer dizer que faltou um parêntese fechando.
