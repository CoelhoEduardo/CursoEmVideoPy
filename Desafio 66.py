soma = contador = 0

while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Foi digitado {contador} numeros \nA soma entre esses numeros digitados foi = {soma} ')
