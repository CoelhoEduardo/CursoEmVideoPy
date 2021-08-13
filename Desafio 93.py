from time import sleep
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
soma = 0
for g in range(0, total):
    partidas.append(int(input(f'   Gols na {g+1}º partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-≃'*50)
print(jogador)
print('-≃'*50)
sleep(1)
for d, p in jogador.items():
    print(f'-{d} = {p}')
print('-≃'*50)
sleep(1)
print(f'O jogador {jogador["Nome"]} jogou {total} partidas.')
for p1, g1 in enumerate(partidas):
    print(f'   => Na partida {p1+1}º, fez {g1}')
print(f'Foi um total de {jogador["Total"]} gols.')

print('THE END')



