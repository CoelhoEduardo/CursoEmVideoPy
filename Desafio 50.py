'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
cont = 0
for p in range(1,7):
    numero = int(input('Digite o {}º valor: '.format(p)))
    if numero %  2 == 0:
        soma +=numero
        cont +=1
print('Você informou {} numeros pares\nA soma desses numero pares = {}'.format(cont, soma))

