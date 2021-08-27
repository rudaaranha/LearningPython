#Ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print('Este programa converte uma distância de metros para centímetros e milímetros.')
d=float(input('Digite uma distância em metros:'))
cent=d*100
mil=d*1000
print('Ao converter a distância {}m, temos o valor de {:.2f}cm e {:.2f}mm.'.format(d,cent,mil))
