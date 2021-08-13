'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print('~-'*20)
print('JOGO DO PAR OU IMPAR!!')
print('~-'*20)
from random import randint
contador = 0
while True:
    numero = int(input('Escolha um numero: '))
    jogador = str(input('Par ou Impar ? [P/I]: ')).upper().strip()[0]
    computador = randint(0,10)
    soma = computador + numero
    if soma % 2 == 0:
        print(f'Player choice: {numero} \nComputer choice: {computador} \nResultado = {soma}... É PAR')
        if jogador == 'P':
            print('VOCÊ VENCEU')
            contador +=1
        else:
            print('VOCÊ PERDEU!')
            break

    else:
        print(f'Player choice: {numero} \ncomputer choice: {computador} \nResultado = {soma}... É IMPAR')
        if jogador == 'I':
            print('VOCÊ VENCEU')
            contador +=1
        else:
            print('VOCÊ PERDEU')
            break
print(f'Você conquistou {contador} vitorias consecutivas ')
