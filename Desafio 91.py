from random import randint
from time import sleep
from operator import itemgetter
jogador = dict()
ranking = dict()
for p in range(0, 4):
    jogador[f'jogador {p+1}'] = randint(1, 6)
for a, i in jogador.items():
    print(f'{a} tirou [{i}] no dado')
    sleep(1)
print("≃"*30)
print(f'{"~=RANKING DOS JOGADORES=~":^30}')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for r, j in enumerate(ranking):
    print(f'{r+1}º lugar: {j[0]} com [{j[1]}]')
