#Ex059 - Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso. A pessoa deve digitar dois números e decidir o que o programa deve fazer.
from time import sleep
print('Este é o programa Haniel. Ele relaiza pequenas operações com dois números de sua escolha.')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
print('Agora no menu de opções abaixo escolha qual tarefa deseja realizar:')
escolha = 0
while escolha != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    escolha = int(input('>>>>>>>>Qual operação você deseja realizar? (de 1 a 5):'))
    if escolha == 1:
        soma = n1 + n2
        print('A soma dos números {} + {} é igual a {}.'.format(n1, n2, soma))
    elif escolha == 2:
        mult = n1 * n2
        print('O produto entre os números {} e {} é igual a {}.'.format(n1, n2, mult))
    elif escolha == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
        elif n1 == n2:
            print('Os números escolhidos são iguais.')
        else:
            print('O número {} é maior que o número {}.'.format(n2, n1))
    elif escolha == 4:
        print('Escolha os números novamente abaixo.')
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
    elif escolha == 5:
        print('O programa está sendo finalizado.')
    else:
        print('Opção inválida. Por favor, tente novamente.')
    print('=-=' * 10)
print('Até mais!')