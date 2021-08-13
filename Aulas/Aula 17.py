num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort()
num.insert(2, 2)
if 9 in num:
    num.remove(9)
else:
    print("Valor não encontrado")
print(num)
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('\n')
print('='*80)
valores = list()
valores.append(5)
valores.append(4)
valores.append(9)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')
print('\n')
print('='*80)
a = [2, 8, 4, 7]
b = a[:]
b[0] = 10
a.pop()
a.insert(1,3)
a.append(6)
print(f'Lista A: {a}')
print(f'Lista B: {b}')
