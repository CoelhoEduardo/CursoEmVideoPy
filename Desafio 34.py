salario = float(input('Me diga o seu salario:R$  '))

'''aumento2 = salario + (salario * 15 / 100)
aumento = salario + (salario * 10 / 100)
if salario > 1250.00:
    print('O seu salario mudou de R${:.2f} para R${:.2f}, um aumento de 10%'.format(salario, aumento))
if salario <= 1250.00:
    print('O seu salario mudou de R${:.2f} para R${:.2f}, um aumento de 15%'.format(salario, aumento2))'''

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O seu salário de R${:.2f} mudou para R${:.2f}'.format(salario, novo))







