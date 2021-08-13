from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} >> ', end=' ')
            cont += p
            sleep(0.5)
        print('THE END')
    else:
        cont = i
        while cont >= f:
            if p == 0:
                p = 1
            print(f'{cont} >> ', end=' ')
            cont -= p
            sleep(0.5)
        print('The End')


contador(1, 10, 1)
contador(10, 0, 2)
print()
print('AGORA É SUA VEZ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

