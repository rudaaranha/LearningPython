#Ex112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
#mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadescev import dado
from utilidadescev import moeda

p = dado.leiadinheiro2('Digite um preço: R$')
moeda.resumo(p, 35, 22)
