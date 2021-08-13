print('Programa de calculo de descontos 5%')

price = float(input('Preço do produto: R$'))
desconto = price - (price * 5 / 100)

print('O Produto que custava R${:.2f}, com desconto de 5% ficou por R${:.2f}'.format(price, desconto))
