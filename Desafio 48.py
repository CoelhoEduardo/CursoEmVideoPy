'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''
soma = 0
conj = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma +=i
        conj +=1
print('A soma de todos os {} numeros impares é {}'.format(conj,soma))
