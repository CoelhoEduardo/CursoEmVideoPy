
from random import randint
from time import sleep

numero = []


def sorteia(n, v):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        valores = randint(n, v)
        numero.append(valores)
        print(f'{valores} ', end='...')
        sleep(0.3)
    print('Pronto!')


def somaPar():
    print()
    soma = 0
    for p in numero:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {numero}, temos {soma}')


sorteia(1, 15)
somaPar()


