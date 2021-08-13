a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas {}, {}, {}, pode formar um triangulo'.format(a, b, c))
else:
    print('As retas {}, {}, {}, NAO PODE formar um triangulo'.format(a, b, c))

