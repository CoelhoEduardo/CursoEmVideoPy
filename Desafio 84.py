lista = list()
data = list()
pesomaior = pesomenor = 0
while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesomaior = pesomenor = data[1]
    else:
        if data[1] > pesomaior:
            pesomaior = data[1]
        if data[1] < pesomenor:
            pesomenor = data[1]

    lista.append(data[:])
    data.clear()
    opcao = str(input('Quer continuar ? [S/N] '))
    if opcao in 'Nn':
        break
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A pessoa mais pesada tem {pesomaior}kg e é o/a ', end='')
for n in lista:
    if n[1] == pesomaior:
        print(f'{n[0]} ',end='...')
print()
print(f'A pessoa mais leve tem {pesomenor}kg e é o/a ', end='')
for n in lista:
    if n[1] == pesomenor:
        print(f'{n[0]} ', end='...')


