#Ex043 -Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso;
#- Entre 18.5 e 25: Peso ideal;
#- 25 até 30: Sobrepeso;
#- 30 até 40: Obesidade;
#- Acima de 40: Obesidade mórbida.
print('Este programa calcula seu IMC e determina se você está abaixo ou acima do peso.')
print('Vamos começar.')
m = int(input('Qual seu peso em kg?')) #massa da pessoa
h = float(input('Agora diga sua altura em metros:')) #altura da pessoa
#O IMC é calculado dividindo o peso pela altura ao quadrado.
imc = m/(h**2)
print('Com um peso de {}Kg e uma altura de {}m, seu IMC é de {:.1f}.'.format(m, h, imc))
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você possui um quadro de OBESIDADE!')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA!')
