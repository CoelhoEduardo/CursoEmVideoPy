
def area(l, c):
    r = l * c
    print(f'A área de um terreno {l} x {c} é de {r}m²')


print('Controle de Terrenos')
print('-'*30)
area(l=float(input('Largura (m): ')),
     c=float(input('Comprimento (m): ')))
