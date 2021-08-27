def metade(n=0):   #calcula a metade de um valor qualquer n.
    p = n / 2
    return p


def dobro(n=0):    #calcula o dobro de um valor qualquer n. Utilizado no ex107
    p = n * 2
    return p


def aumentar(n=0, x=0):    #calcula um valor n qualquer aumentado em x porcento. Utilizado no ex107
    p = n + (n * (x/100))
    return p


def diminuir (n=0, x=0):   #calcula um valor n qualquer diminuido em x porcento. Utilizado no ex107
    p = n - (n * (x/100))
    return p


def moeda(n=0, moeda ='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',') #Tem como fazer um return formatado
