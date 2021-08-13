contadorIdade = contadorMasculino = contadorFeminino = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contadorIdade += 1
    if sexo == 'M':
        contadorMasculino += 1
    if idade < 20 and sexo == 'F':
        contadorFeminino += 1

    print('-' * 20)
    programa = ' '
    while programa not in 'SN':
        programa = str(input('Deseja cadastrar mais dados? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if programa == 'N':
        break
print(f'Tem {contadorIdade} pessoas com mais de 18 anos')
print(f'Tem {contadorMasculino} homens cadastrados')
print(f'Tem {contadorFeminino} mulheres com menos de 20 anos')
