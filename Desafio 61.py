'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('PROGRESSÃO ARITMÉTICA V2.0')
pt = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
termo = pt
contador =1

while contador <= 10:
    print('{} >>> '.format(termo),end=' ')
    termo +=r
    contador +=1

print("The End")



