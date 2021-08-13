'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
print('\033[33m*=*'*50)
print('{:^150}'.format('\033[33mJOKENPÔ'))
print('*=*'*50)
import random
import time
itens = ('Pedra','Papel','Tesoura')
computador = random.randint(0,2)
print('''OPÇÕES DE JOGADAS
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('SUA JOGADA: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('\033[33m*=*'*12)
print('\033[35mCOMPUTADOR: {}'.format(itens[computador]))
print('\033[31mPLAYER: {}'.format(itens[jogador]))
print('\033[33m*=*'*12)
if computador == 0:
    if jogador == 0:
        print('\033[7mEMPATE')
    elif jogador == 1:
        print('\033[7mPLAYER WIN')
    elif jogador == 2:
        print('\033[7mCOMPUTADOR WIN')
    else:
        print('\033[7mOPÇÃO INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[7mCOMPUTADOR WIN')
    elif jogador == 1:
        print('\033[7mEMPATE')
    elif jogador == 2:
        print('\033[7mPLAYER WIN')
    else:
        print('\033[7mOPÇÃO INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[7mPLAYER WIN')
    elif jogador == 1:
        print('\033[7mCOMPUTADOR WIN')
    elif jogador == 2:
        print('\033[7mEMPATE')
    else:
        print('\033[7mOPÇÃO INVALIDA')
