'''Desafio 22'''
Nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo: {}'.format(Nome.upper()))
print('Seu nome em minusculo: {}'.format(Nome.lower()))
print('O seu nome tem {} letras'.format(len(Nome) - Nome.count(' ')))
print('O seu primeiro tem {} letras'.format(Nome.find(' ')))
primeiro = Nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro[0],len(primeiro[0])))





















