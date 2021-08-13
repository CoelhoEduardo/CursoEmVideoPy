''' Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

Numero = int(input('Digite um numero inteiro qualquer: '))
print('''AS OPÇÕES PARA CONVERSÃO: 
*1* PARA BINARIO 
*2* PARA OCTAL 
*3* PARA HEXADECIMAL''')
conver = int(input('Digite sua opção: '))
if conver == 1:
      print('{} convertido para Binario = {}'.format(Numero, bin(Numero)[2:]))
elif conver == 2:
    print('{} convertido para Octal = {}'.format(Numero, oct(Numero)[2:]))
elif conver == 3:
    print('{} convertido para Hexadecimal = {}'.format(Numero, hex(Numero)[2:]))
else:
    print('DOENTE MENTAL, NÃO EXISTE ESSA OPÇÃO')

