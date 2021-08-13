'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''

N = int(input('Digite um valor: '))
pvalor = 1
svalor = 2
print('{} >>> {} >>>'.format(pvalor, svalor),end=' ')
contador = 4
while contador <= N:
    tvalor = pvalor + svalor
    print('{} >>> '.format(tvalor), end=' ')
    pvalor = svalor
    svalor = tvalor
    contador +=1
print('The End')

