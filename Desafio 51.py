'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
pt = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
seq = pt + (10 - 1) * r
for pa in range(pt,seq + r,r):
    print('{} -->'.format(pa), end=' ')
print('FINISH')
