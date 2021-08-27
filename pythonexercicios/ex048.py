#Ex.048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
print('Este programa calcula a soma entre todos os número ímpares múltiplus de 3 no intervalo entre 1 e 500.')
cont = 0
soma = 0
for n in range(3, 501, 3):
    if n % 3 == 0 and n % 2 != 0:
        cont = cont + 1 #contador. vai contar os números e a partir do momento em que for encontrando números, vai somando uma unidade. nesse caso serão 83 números identficados.
        soma = soma + n #acumulador. Vai acumulando os valores, seja pela soma, seja pela multiplicação. nesse caso foram acumulados por meio da adição (20667)
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))

#para a soma e o contador (cont), eles podem fazer assim também:
# soma += c
# cont += 1