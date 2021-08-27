#Ex102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
#o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
#ou não na tela o processo de cálculo do fatorial.
def fatorial(num=1, show=False):
    """-> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não o cálculo realizado.
        :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            if c != 1:
                print(f'{c} x ', end='')
                f = f * c
            else:
                print(f'{c} = ', end='')
                f = f * c
        return f
    if show == False:
        for c in range(num, 0, -1):
            f = f * c
        return f


#Programa principal
print(fatorial(5, show=True))
print(fatorial(5, show=False))
print(fatorial(5))
help(fatorial)
