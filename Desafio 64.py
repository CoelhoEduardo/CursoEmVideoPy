'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = contador = total = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    total += n
    contador += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} e a soma entre eles é = {}'.format(contador, total))

