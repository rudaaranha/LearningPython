#Ex006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('Este algoritmo mostra o dobro, o triplo e a raiz quadrada de um número qualquer. \nSendo assim...')
n=float(input('Digite um número qualquer:'))
dob=n*2
tri=n*3
raiz=n**0.5
print('O dobro do número {} é {:.2f}; \nSeu triplo é {:.2f}; \ne sua raiz quadrada é {:.2f}'.format(n, dob, tri, raiz))
