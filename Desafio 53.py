'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for p in range (len(junto) -1,-1,-1):
    inverso += junto[p]
print(junto, inverso)
if inverso == junto:
    print('A frase acima é um PALÍNDROMO')
else:
    print('A frase acima não é UM PALÍNDROMO')

#SEM O CONCEITO DE LAÇO

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')

