
def título(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))


título('  CURSO EM VÍDEO ')
título('  APRENDA PYTHON ')
título('  TRABALHE COM PYTHON ')

print('-~'*1000)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
print()
print()


def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('Fim!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam}')


contador(2, 3, 4)
contador(3, 1, 5, 6)
contador(1, 3, 7, 5, 8)
print()
print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print()
print()


def somad(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somad(2, 4, 5, 4)
somad(2, 3, 1, 3)
somad(2, 3)
somad(10, 4)

