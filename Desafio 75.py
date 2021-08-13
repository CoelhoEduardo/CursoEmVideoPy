

numbers = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),int(input('Digite um numero: ')))

print(f'Você escolheu os numeros: {numbers}')
print(f'O numero 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O numero 3 apareceu na {numbers.index(3)+1}º posição ')
else:
    print(f'O numero 3 não foi digitado')
print(f'O numeros pares são: ',end=' ')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')
