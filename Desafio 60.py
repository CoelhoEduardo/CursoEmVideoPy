
import math
n = ''
numero = int(input('Digite um numero para calcular seu fatorial: '))
while n != 1:
    fatorial = math.factorial(numero)
    print('Calculando {}!'.format(numero), end='= ')
    for n in range(numero, 0, -1):
        print('{} '.format(n), end='')
        print('x ' if n > 1 else '= {}'.format(fatorial), end='')



