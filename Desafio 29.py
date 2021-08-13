velocidade = float(input('Velocidade do carro:'))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! Você excedeu a velocidade maxima de 80km')
    print('Sua multa sera no valor de {:.2f}'.format(multa))
else:
    print('Tenha um bom dia ! Dirija com segurança!')
    