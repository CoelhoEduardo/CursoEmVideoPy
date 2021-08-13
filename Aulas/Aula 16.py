lanche = ('Hambúrguer', 'Suco', 'Batata Frita', 'Pudim', 'Pizza')

print(lanche[0], lanche[-1])
#Tuplas SÃO IMUTÁVEIS
for cont in range(0, len(lanche)):
    print(f'vamos comer {lanche[cont]} na posição {cont}')

for comida in lanche:
   print(comida)

for pos, comida, in enumerate(lanche):
    print(f'Irei comer {comida} nessa ordem {pos}')
print(sorted(lanche))
'''---------------------------------------------------------------------------------------'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(len(c))
print(c.count(5))
print(b.index(8))
'''----------------------------------------------------------------------------------'''
pessoa = ('Eduardo', 23, 'M', 71.10)
print(pessoa)