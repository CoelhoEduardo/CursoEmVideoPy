numero = []
contador = 0
while True:
    numero.append(int(input('Digite um valor: ')))
    contador += 1
    numero.sort(reverse=True)
    opcao = str(input('Deseja continuar ? [S/N]: '))
    if opcao in 'Nn':
        break
print(f'Você digitou {contador} numeros') #podia ter usado o len(valores)
print(f'Os valores em ordem decrescente : {numero}')
if 5 in numero:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')





