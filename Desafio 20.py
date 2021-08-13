import random
a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2: '))
a3 = str(input('Nome do Aluno 3: '))
a4 = str(input('Nome do Aluno 4: '))
a5 = input('Nome do Aluno 5: ')
a6 = input('Nome do Aluno 6: ')
'''lista = [a1,a2,a3,a4]
random.shuffle(lista)
print(lista)'''

print('a ordem: {}'.format(random.sample([a1,a2,a3,a4, a5], k=4)))


