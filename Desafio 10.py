print('CONVERSOR DE MOEDAS')

real = float(input('Quantidade de dinheiro = R$'))
Dolar = real/ 5.42
Euro = real/ 6.62
ienes = real/0.0521
libra = real/7.35
print('Com R${} pode comprar ${:.2f}'.format(real, Dolar))
print('Com R${} pode comprar {:.2f} Euros'.format(real, Euro))
print('Com R${} pode comprar {:.2f} Ienes'.format(real,ienes))
print('Com R${} pode comprar {:.2f} Libras'.format(real,libra))




