'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:'''
menu = ''
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
while menu != 5:
    menu = int(input(' [1] SOMAR\n [2] MULTIPLICAR\n [3] MAIOR\n [4] NOVOS VALORES\n [5] OUT\n>>>>>>>>Qual é a sua opção: '))

    if menu == 1:
       print('{} + {} = {}'.format(primeiro, segundo,primeiro + segundo))
    elif menu == 2:
        print('{} * {} = {}'.format(primeiro, segundo, primeiro * segundo))
    elif menu == 3:
        if primeiro > segundo:
            print('O maior numero é: {}'.format(primeiro))
        else:
            print('O maior numero é: {}'.format(segundo))
    elif menu == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif menu == 5:
        print('Adeus e até a proxima')
    else:
        print('Opção invalida... Tente novamente...')
