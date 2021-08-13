print('Programa para calcular aumento de 15% no salario')

salario = float(input('Salario atual: R$ '))

aumento = salario + (salario * 15 / 100)

print('O seu salario de R${:.2f}, com aumento de 15%, será de R${:.2f} '.format(salario, aumento))
