time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na {c+1}º partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        programa = str(input('Quer continaur ? [S/N] ')).upper()[0]
        if programa in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if programa == 'N':
        break
print('-=' *30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 = break) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No {i+1}º jogo fez {g} gols')
    print('-'*40)

print('<<Volte Sempre>>')

