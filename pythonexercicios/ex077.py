#Ex077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'Curso', 'Grátis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoóõôu':
            print(letra, end=' ')
