import time
from random import randint
print('-#'*50)
print('                         JOGA NA MEGA SENA                         ')
print('-#'*50)
ndejogos = int(input('Quantos jogos você quer eu sorteie ? '))
print('-#'*50)
for n in range(0, ndejogos):
    jogos = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    time.sleep(0.5)
    jogos.sort()
    print(f'jogo {n+1}: {jogos}')
print('-#'*50)
print('                         JOGOS SORTEADOS, BOA SORTE                        ')


#------------------------------------------RESOLUÇÃO DO PROF -----------------------------------------#
lista = list()
jogos1 = list ()
quant = int(input('Quantos jogos voce quer que eu sorteie ? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos1.append(lista[:])
    lista.clear()
    tot += 1
print(f'sorteando {quant} jogos')
for i, l in enumerate(jogos1):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)

