#exemplo para condições if(se) e else(senão)
tempo=int(input('Quantos anos tem seu carro?'))
if tempo <=3: #sempre usar if:(if dois pontos) e else:(else dois pontos)
    print('Carro novo') #Quando a frase inicia com tab (ou seja, não está colada) ela só aparece dependendo de uma condição. diferente do print('fim') que sempre vai aparecer(está colado)
else:
    print('Carro velho') #Ou o carro é novo(menos ou igual a 3 anos) ou o carro é velho (mais de 3 anos, nesse caso o senão)
print('--FIM--') #dependendo da idade do carro, duas possibilidades de resposta são possíveis

#outra forma de escrever esse programa seria da forma simplificada (condição simplificada)
tempo=int(input('Quantos anos tem seu carro?'))
print('Carro novo'if tempo<=3 else 'Carro velho')
print('--FIM--')

print('-'*130)

nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

print('-'*130)

nome=str(input('Qual é o seu nome?'))
if nome == 'Rudá':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

print('-'*130)

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m>=6.0:
    print('Parabéns, você foi aprovado!')
else:
    print('Que pena, mas você foi reprovado.')

print('-'*130)

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A sua média foi {:.1f}.'.format(m))
print('Parabéns!' if m>=6.0 else 'Estude mais!')
