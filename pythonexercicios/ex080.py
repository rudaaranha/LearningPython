#Ex080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
num = list()
maior = menor = 0
for c in range(0, 5):
    n = int(input('Digite um número: ')) #a variável n não pode ser igual ao contador
    if c == 0 or n > num[-1]:
        num.append(n)
        print('O valor foi adicionado ao final da lista...')
    else:
        x = 0 #posição começa em 0
        while x < len(num):  #enquanto a posição foi menor que o tamanho da lista.
            if n <= num[x]: #se n for menor ou igual a lista na posição x...
                num.insert(x, n) #inserir o elemento n na lista na posição x.
                print(f'Valor adicionado na posição {x}.')
                break
            x = x + 1 #aumentar o posição de x sempre que o laço for repetido
print('-='*30)
print(f'Os valores digitados na ordem foram {num}.')
