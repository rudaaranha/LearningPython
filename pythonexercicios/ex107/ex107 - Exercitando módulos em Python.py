#Ex107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas
#aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe
#esse módulo e use algumas dessas funções.
import moeda   #a importação só é possível porque ambos os arquivos estão no mesmo diretório.

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}.')
print(f'O dobro de R${p} é R${moeda.dobro(p)}.')
print(f'Aumentando em 10%, temos R${moeda.aumentar(p, 10)}.')  #10 é o valor em % a ser aumento de p
print(f'Reduzindo em 13%, temos R${moeda.diminuir(p, 13)}.')   #13 é o valor em % a ser diminuido de p