'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

pt = int(input('Coloque o primeiro termo: '))
r = int(input('Insira a razão: '))
termo = pt
contador = 1
total = 0
morept = 10
while morept != 0:
    total += morept
    while termo != 0 and contador <= total:
        print('{} >>>'.format(termo),end=' ')
        termo +=r
        contador += 1
    print('Pausa')
    morept = int(input('Quantos termos você quer mostrar mais? '))
print('The End! :D')
print('Total de termos calculados: {}'.format(total))
