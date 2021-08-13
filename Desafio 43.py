'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:'''
altura = float(input('Qual é a sua altura? (m) '))
peso = float(input('Qual é o seu peso? (kg) '))
imc = peso / (altura ** 2)

print('Seu IMC = {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso normal, CUIDADO')
elif 18.5 <= imc < 25:
    print('PARABENS, Peso ideal')
elif 25 <= imc < 30:
    print('SOBREPESO, fique atento')
elif 30 <= imc < 40:
    print('ATENÇÃO, OBESO')
elif imc >= 40:
    print('OBESIDADE MORBIDAM, VÁ SE CUIDAR')

