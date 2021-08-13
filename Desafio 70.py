totalcompra = maiscaro = maisbarato = contador = 0
produtobarato = ''
while True:
    produto = str(input('Nome Do Produto: '))
    preco = float(input('Preço do Produto: R$ '))
    contador +=1
    if preco >= 1000:
        maiscaro += 1
    totalcompra += preco
    if contador == 1 or preco < maisbarato:
        maisbarato = preco
        produtobarato = produto
    programa = ' '
    while programa not in 'SN':
        programa = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if programa == 'N':
        break

print(f'Total gasto em compras: R${totalcompra:.2f}')
print(f'Total de produtos acima de R$1000: {maiscaro}')
print(f'O produto mais barato foi {produtobarato} que custa apenas R${maisbarato:.2f}')
