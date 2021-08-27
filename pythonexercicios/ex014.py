#Ex014 - Escreva um programa que converta uma temperatura digitada em °C para °F.
print('Este programa converte a temperatura de °C para °F')
tc=float(input('Digite a temperatura em °C:'))
tf=((9/5)*tc)+32
print('Para {}°C, tem-se um valor de {}°F'.format(tc,tf))
