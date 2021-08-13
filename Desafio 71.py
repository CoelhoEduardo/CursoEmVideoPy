nota50 = nota20 = nota10 = nota5 = nota2 = 0
print('$'*50)
print('{:^50}'.format('$BANCO PORTUGA$'))
print('$'*50)
while True:
    saque = int(input('Qual será o valor a ser sacado: R$'))
    while saque >= 50:
        nota50 += 1
        saque -= 50

    while saque >= 20:
        nota20 += 1
        saque -= 20

    while saque >= 10:
        nota10 += 1
        saque -= 10

    while saque >= 5:
        nota5 += 1
        saque -= 5


    while saque >= 2:
        nota2 += 1
        saque -= 2

    if nota50 >= 1:
        print(f'Total de {nota50} cédulas de R$ 50')
    if nota20 >= 1:
        print(f'Total de {nota20} cédulas de R$ 20')
    if nota10 >= 1:
        print(f'Total de {nota10} cédulas de R$ 10')
    if nota5 >= 1:
        print(f'Total de {nota5} cédulas de R$ 5')
    if nota2 >= 1:
        print(f'Total de {nota2}  cédulas de R$ 2')
    break
print('$'*50)
print('VOLTE SEMPRE MA NIGGA! $ _ $ ')

