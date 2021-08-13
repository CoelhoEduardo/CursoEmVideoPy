'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

#minha resposta
'''sexo = str(input('Digite o seu sexo[M / F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Try Again')
    sexo = str(input('Digite o seu sexo [M / F]: ')).upper()

print('Thanks')
print('End program')'''

#Resposta do professor
sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Tente novamente: ')).strip().upper()[0]
print('Dados registrado com sucesso, voce é do sexo {}'.format(sexo))
