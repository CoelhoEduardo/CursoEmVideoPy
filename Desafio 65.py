opcao = 'S'
contador = soma = media = maior = menor = 0
while opcao in 'Ss':
    numeros = int(input('Digite um número: '))
    contador+=1
    soma +=numeros
    if contador == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    opcao = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    media = soma / contador
print('Você digitou {} e a média foi {}'.format(contador, media))
print('O Maior valor foi {} e o menor foi {}'.format(maior, menor))
