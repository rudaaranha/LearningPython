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
1

def moeda(n=0, moeda ='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',') #Tem como fazer um return formatado


#RESOLUÇÃO DO PROFESSOR - ex109

#def metade(n=0, sit=False):   #calcula a metade de um valor qualquer n.
#    p = n / 2
#    return p if sit is False else moeda(p) #interessante colocar tudo na mesma linha como se fosse uma frase mesmo


#def dobro(n=0, sit=False):    #calcula o dobro de um valor qualquer n. Utilizado no ex107
#    p = n * 2
#    return p if sit is False else moeda(p)


#def aumentar(n=0, x=0):    #calcula um valor n qualquer aumentado em x porcento. Utilizado no ex107
#    p = n + (n * (x/100))
#    return p if sit is False else moeda(p)


#def diminuir (n=0, x=0):   #calcula um valor n qualquer diminuido em x porcento. Utilizado no ex107
#    p = n - (n * (x/100))
#    return p if sit is false else moeda(p)


#def moeda(n=0, moeda ='R$'):
#    return f'{moeda}{n:.2f}'.replace('.', ',') #Tem como fazer um return formatado
