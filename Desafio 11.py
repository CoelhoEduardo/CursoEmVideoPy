print('PROGRAMA DE CALCULO DE TINTA')
larg = float(input('Largura da sua parede: '))
alt = float(input('Altura da sua parede: '))
m2 = alt * larg

tinta = m2 / 2

print('Sua parede tem de dimensão {}x{} que em m² = {:.2f}m²'.format(alt, larg, m2))
print('Para pintar sua parede será necessario {:.2f}L de tinta'.format(tinta))
