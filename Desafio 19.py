import random
a1 = input('Nome do Aluno1: ')
a2 = input('Nome do Aluno2: ')
a3 = input('Nome do Aluno3: ')
a4 = input('Nome do aluno4: ')
lista = [a1, a2, a3, a4]

sorteio = random.choice(lista)
print('O aluno sorteado é {}'.format(sorteio))