#Agora vamos considerar várias condições (não só duas como nas condições simples usando if). O if só permite duas condições... ou é verdadeiro(if) ou falso(else).
#Estrutura aninhada é a existência de uma estrutura condicional dentro de outra estrutura condicional.
#Quando existem 3 possibilidades usa-se o if condição1:; o elif(else if) condição:; e o else:
#Se por acaso forem 4 condições, usa-se mais um elif. (if:, elif:, elif:, else:)
#Else só pode ser usada nenhuma ou apenas uma vez, enquanto o elif pode ser utilizado quantas vezes quiser...
#Nunca será possível usar elif ou else sem um if antes.


#AULA 12
#Estrutura condicional simples (utilizando apenas o if)
nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))

#Estrutura condicional composta (condição utilizando if e else)
nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Estrutura condicional aninhada 1 (condição utilizando um elif e else)
nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Estrutura condicional aninhada 2 (condição utilizando dois elifs e else)
nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Claudia, Jéssica, Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

#Estrura condicional aninhada 3 (utilizando dois elifs, porém sem o else)
nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana, Claudia, Jéssica, Juliana':
    print('Belo nome feminino.')
print('Tenha um bom dia, {}!'.format(nome))
