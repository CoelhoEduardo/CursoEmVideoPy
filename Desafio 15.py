print('PROGRAMA ALUGUEL DE CARRO')

road = float (input('Quantos KM percorridos: '))
dias = int(input('Quantos dias usado: '))

total = (road * 0.15) + (dias *  60)

print('Total a pagar pelo o carro = R$ {:.2f}'.format(total))

