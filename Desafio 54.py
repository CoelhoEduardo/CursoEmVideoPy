'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for a in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}º Pessoa: '.format(a)))
    idade = atual - ano
    if idade >= 18:
        cont1 +=1
    else:
        cont2 +=1

print('\033[32mMaiores de idade: {}'.format(cont1))
print('\033[31mMenores de idade: {}'.format(cont2))

