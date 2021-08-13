y = int(input('Primeiro numero: '))
x = int(input('Segundo numero: '))
z = int(input('Terceiro numero: '))
menor = y
if x < y and x < z:
    menor = x
if z < y and z < x:
    menor = z

maior = y
if x > y and x > z:
    maior = x
if z > y and z > x:
    maior = z

print('o MENOR numero é: {}'.format(menor))
print('o MAIOR numero é: {}'.format(maior))





