#O código para adicionar cores no terminal é do tipo: \033[0;33;44m
#O 033 indica o melhor código para cores que funciona no python. O 0 indica o estilo (0-nenhum; 1-negrito; 4-sublinhado e 7-negativo)
#O 30 indica a cor do texto, variando de 30 a 37.(30-branco;31-vermelho;32-verde;33-amarelo;34-azul;;35-magenta;36-ciano e 37-cinza).
#O 44 indica a cor do fundo, variando de 40 a 47 e seguindo a mesma orientação das cores do texto.
#também existe o módulo corilize
#Se quiser voltar para o padrão do terminal(sem estilo, letra cinza e fundo preto), usar o código \033[m
#E para utilizar texto na cor preta, deve-se usar o código de inversão e letra branca. \033[7;30m

print('\033[31mOlá, mundo!') #letra vermelha
print('\033[31;43mOlá, mundo!') #letra vermelha e fundo amarelo
print('\033[1;31;43mOlá, mundo!') #letra vermelha, fundo amarelo e em negrito
print('\033[1;31;43mOlá, mundo!\033[m') #letra vermelha, fundo amarelo e em negrito, porém o fundo amarelo só fica na frase. (para isto adicionar o \033[m no fim da frase
print('\033[4;30;45mOlá, mundo!\033[m') #letra branca, fundo lilás e sublinhado(fundo até o fim da frase)
print('\033[30mOlá, mundo!') #letra branca
print('\033[7;30mOlá, mundo!\033[m') #letra preta e fundo branco (ultizando o estilo negativo)
print('--='*50)
a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}!\033[m'.format(a,b)) #deixar as variáveis coloridas. Perceba que o "e" e o "!" saiu amarelo também... para corrigir isso
a = 2
b = 4
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))
print('--='*50)
#por fim...
nome = 'Rudá'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m' )) #adicionar colchetes antes e depois da variável (como se fossem novas variáveis)
print('--='*50)
nome = 'Rudá'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}
print('Olá! Prazer em te conhecer, {}{}{}!'.format(cores['pretobranco'], nome, cores['limpa']))