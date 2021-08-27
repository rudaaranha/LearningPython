#Ex062 - Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.\
#nesse problema nós vamos ter laços aninhados

print('     GERADOR DE PA     ')
print('='*30)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1 #contagem... nesse caso sendo 1
total = 0 #sempre que eu adicionar uma variável no laço, esta tem que aparecer fora dele como uma contagem.
mais = 10 #a primeira volta do laço sempre vai ocorrer com 10 (pois mais = 10 e total = 0),
while mais != 0:
   total = total + mais
   while cont <= total:
      print('{} - '.format(termo), end='')
      termo += razão
      cont += 1
   print('PAUSA')
   mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')


print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
x = int(input('Primeiro termo:'))
y = int(input('Razão:'))
décimo = x + (10 - 1) * y
pa = x
cont = y
mais = 1
total = 0
print('{} - '.format(pa), end='')
while mais != 0:
   total = total + décimo
   while pa < décimo:
      pa = pa + cont
      print('{}'.format(pa), end=' - ')
   mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')