
def ficha(j="<desconhecido>", gol=0):
    print(f'O jogador {j} fez {gol} gol(s) na temporada.')


n = str(input('Nome do Jogador: '))
g = input('Numero de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)









