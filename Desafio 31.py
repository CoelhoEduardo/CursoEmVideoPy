viagem = float(input('A distancia da sua viagem? '))
passagem1 = viagem * 0.50
passagem2 = viagem * 0.45
if viagem <= 200:
    print('Você fará uma viagem de {}'.format(viagem))
    print('Sua passagem ficara no valor de R${:.2f}'.format(passagem1))
else:
    print('Sua viagem será de {} KM'.format(viagem))
    print('Sua passagem será de R${:.2f}'.format(passagem2))

