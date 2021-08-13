import math
adj = float(input('comprimento do cateto adjacente: '))
opos = float(input('comprimento do  cateto oposto: '))
print('Hipotenusa = {:.2f} '.format(math.hypot(adj, opos)))

