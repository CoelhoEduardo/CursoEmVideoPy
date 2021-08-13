'''O FAMOSO CALCULO DE MÉDIA DE ALUNO'''
aluno = input('Nome do Aluno: ')
n1 = float(input('A Primeira nota: '))
n2 = float(input('A Segunda nota: '))
media = (n1 + n2) / 2
print('A media entre as notas {} e {}, é igual á {}'.format(n1, n2, media))
if media < 5:
    print('Aluno REPROVADO')
elif 7 > media >= 5:
    print('ALuno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')
