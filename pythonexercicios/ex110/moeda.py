def metade(n=0, sit=False):   #calcula a metade de um valor qualquer n.
    p = n / 2
    if sit == True:
        return moeda(p)#f'R${p:.2f}'.replace('.', ',')
    else:
        return p


def dobro(n=0, sit=False):    #calcula o dobro de um valor qualquer n. Utilizado no ex107
    p = n * 2
    if sit == True:
        return moeda(p) #f'R${p:.2f}'.replace('.', ',')
    else:
        return p


def aumentar(n=0, x=0, sit=False):    #calcula um valor n qualquer aumentado em x porcento. Utilizado no ex107
    p = n + (n * (x/100))
    if sit == True:
        return moeda(p) #f'R${p:.2f}'.replace('.', ',')
    else:
        return p


def diminuir (n=0, x=0, sit=False):   #calcula um valor n qualquer diminuido em x porcento. Utilizado no ex107
    p = n - (n * (x/100))
    if sit == True:
        return moeda(p) #f'R${p:.2f}'.replace('.', ',')
    else:
        return p


def moeda(n=0, moeda ='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',') #Tem como fazer um return formatado


def resumo(n, a=10, d=5):
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-' * 30)
