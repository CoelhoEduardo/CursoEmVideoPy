'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:'''
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas acima, PODE formar um triangulo ',  end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('As retas {}, {}, {}, NAO PODE formar um triangulo '.format(a, b, c))