
def maior(*num):
    maior = cont = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(4, 3, 2, 1, 0)
print()
maior(0, 5, 6)
print()
maior(0, 1, 8, 12)
