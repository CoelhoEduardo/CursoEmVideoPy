Brasileirao = ('Flamengo', 'Internacional', 'Atletico - MG', 'São Paulo', 'Fluminense',
               'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC',
               'Corinthians','Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza','Vasco da Gama',
               'Goiás', 'Coritiba', 'Botafogo')
print('='*40)
print(f'Os cincos primeiros colocados do Brasileirão: {Brasileirao[0:5]}')
print('='*40)
print(f'Os 4 ultimos colocados do Brasileirão: {Brasileirao[-4:]}')
print('='*40)
print(f'Times em Ordem Alfabetica: {sorted(Brasileirao)}')
print('='*40)
print(f'O Corinthians está na posição: {Brasileirao.index("Corinthians")+1}º')
print('='*40)