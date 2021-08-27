#Ex113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
#digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue     #O continue serve para retornar ao laço em caso de erro(while True)
        except(KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n1


n = leiaint('Digite um número inteiro: ')
n1 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e número real foi {n1:.2f}.')
