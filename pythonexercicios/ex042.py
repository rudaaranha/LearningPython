#Ex042 - Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais;
#- Isósceles: dois lados iguais;
#- Escaleno: todos os lados diferentes.
print('Este programa lê o comprimento de três retas, diz se elas podem formar um triângulo e se possível, diz que tipo de tria^ngulo é formado.')
r1 = float(input('Qual o comprimento da primeira reta em mm?'))
r2 = float(input('E da segunda reta?'))
r3 = float(input('E da terceira reta?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As retas acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('Como {} é igual a {} que é igual a {}. O triângulo é EQUILÁTERO!'.format(r1, r2, r3))
    elif r1 == r2 != r3:
        print('Como {} é igual a {}, mas é diferente de {}. O triângulo é ISOSCELES!'.format(r1, r2, r3))
    elif r2 == r3 != r1:
        print('Como {} é igual a {}, mas é diferente de {}. O triângulo é ISOSCELES!'.format(r2, r3, r1))
    elif r3 == r1 != r2:
        print('Como {} é igual a {}, mas é diferente de {}. O triângulo é ISOSCELES!'.format(r2, r1, r2))
    elif r1 != r2 and r2 != r3 and r1 != r3: #poderia ser feito r1 != r2 != r3 != r1
        print('Como {}, {} e {} são diferentes entre sí, o triângulo é ESCALENO!'.format(r1, r2, r3))
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo!')
