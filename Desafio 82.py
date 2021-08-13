lista1 = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    par = n % 2
    if par == 0:
        lista2.append(n)
    else:
        lista3.append(n)

    r = str(input('Quer continar ? [s/n] '))
    if r in 'Nn':
        break
print(f'Lista com todos os numeros: {lista1}')
print(f'Lista com os números PARES: {lista2}')
print(f'Lista com os números Ímpares: {lista3}')