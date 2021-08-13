'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
 para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

print('-='*10)
print('Tabuada 3.0')
print('-='*10)
print('*-'*50)
print('Escolha um numero para calcular a tabuada, Caso queira parar digite um valor NEGATIVO')
print('*-'*50)
while True:
    numero = int(input('TABUADA DE: '))
    if numero < 0:
        break
    for n in range(1,11):
        print(f'{numero} x {n:2} = {numero*n}')
    print('-'*30)
print('The End')
