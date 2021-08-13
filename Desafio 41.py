'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:'''
from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Esta na categoria: MIRIM')
elif idade <= 14:
    print('Esta na categoria: INFANTIL')
elif idade <= 19:
    print('Esta na categoria: JUNIOR')
elif idade <= 25:
    print('Esta na categoria: SENIOR')
else:
    print('Esta na categoria: MASTER')
