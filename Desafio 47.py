'''Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''
from time import sleep
for par in range(1+1, 50, 2):
    print(par, end=' ')
    sleep(0.2)
print('THE END')


