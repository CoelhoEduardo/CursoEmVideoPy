maior = menor = 0
valores = list()
for v in range(0,5):
    valores.append(int(input(f'Digite valor para a posição {v}: ')))
    if v ==0:
        maior = menor =valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor da lista é {maior} que esta localizado nas posições...', end='')
for i, c in enumerate(valores):
    if c == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor da lista é {menor} que esta localizado nas posições...', end='')
for i, c in enumerate(valores):
    if c == menor:
        print(f'{i}...', end='')
print()
