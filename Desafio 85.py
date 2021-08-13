numeros = [[], []]

valores = 0
for p in range (1, 8):
    valores = int(input(f'Digite o {p}º valor: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares = {numeros[0]}')
print(f'Os valores impares = {numeros[1]}')

