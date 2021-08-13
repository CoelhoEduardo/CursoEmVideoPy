'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:'''

print('{:=^40}'.format('COELHO CASEIRO'))
preco = float(input('Valor do Produto: R$ '))
print('Valor da Compra: R$ {:.2f}'.format(preco))
print('''FORMAS DE PAGAMENTO: 
[1] A VISTA/DINHEIRO: 10% DE DESCONTO 
[2] CARTÃO DE DEBITO: 5% DE DESCONTO 
[3] 2X NO CARTÃO: PREÇO NORMAL 
[4] 3X OU MAIS NO CARTAO: 20% DE JUROS''')
pagamento = int(input('Forma de pagamento: '))
if pagamento == 1:
    total = preco - (preco * 10 / 100)
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print('O valor á ser pago em 2x SEM JUROS = R$ {:.2f}'.format(parcela))
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas: '))
    parcelado = total/parcelas
    print('O valor sera pago em {}x COM JUROS no cartão = R$ {:.2f}'.format(parcelas, parcelado))
else:
    total = preco
    print('Opção de pagamento invalido. Tente novamente')
print('O valor da compra R${:.2f}, valor final R${:.2f}'.format(preco, total))
