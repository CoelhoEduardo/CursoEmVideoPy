''' Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. '''

casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salario? R$ '))
anos = int(input('Em quantos anos deseja pagar? '))

minimo = salario * 30 / 100
parcelas = anos * 12
prest = casa/parcelas

print('A casa no valor de R$ {:.2f} será parcelada em {}x de R$ {:.2f}'.format(casa, parcelas, prest))
if prest > minimo:
    print('Emprestimo Negado')
elif prest <= minimo:
    print('Emprestimo Aprovado')
