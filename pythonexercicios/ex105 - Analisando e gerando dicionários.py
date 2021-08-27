#Ex105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
#vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    tot = maior = media = menor = soma = 0
    for c in n:
        tot = tot + 1
        if tot == 1:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        soma = soma + c
        média = soma/tot
    if sit == True:
        if média < 4:
            cadernonotas = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': média, 'Situação': 'RUIM'}
        elif 4 <= média < 7:
            cadernonotas = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': média, 'Situação': 'RAZOÁVEL'}
        elif 7 <= média < 8.5:
            cadernonotas = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': média, 'Situação': 'BOA'}
        elif média >= 8.5:
            cadernonotas = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': média, 'Situação': 'EXCELENTE'}
    else:
        cadernonotas = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': média}
    print(cadernonotas)


#Programa principal
notas(9, 8, 9, sit=True)
#help(notas)

#---------------------------------------------------------
#Resolução do professor
#def notas(*n, sit=False):
#   r = dict()
#   r['total'] = len(n)
#   r['maior'] = max(n)
#   r['menor'] = min(n)
#   r['média'] = sum(n)/len(n)
#   if sit:
#       if r['média'] >= 7:
#           r['sitiação'] = BOA
#       elif r['média'] >= 5:
#           r['sitiação'] = RAZOÁVEL
#       else:
#           r['sitiação'] = RUIM
#   return r
#
#
#Programa principal
#resp = notas(5.5, 2.5, 1.5, sit=True)
#print(resp)
