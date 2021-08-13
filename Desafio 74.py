from random import randint

numbers = (randint(1, 9),  randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

print('Numeros sorteados: ', end=' ')
for sequencia in numbers:
    print(sequencia, end=' ')

print(f'\nO maior numero sorteado = {max(numbers)}')
print(f'O menor numero sorteado = {min(numbers)}')
