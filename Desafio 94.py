pessoas = dict()
dados = list()
media = soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MmFf':
        print('Erro! Por favor, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    programa = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
    while programa not in 'SsNn':
        print('Erro! Por favor, Responda apenas S ou N.')
        programa = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
    if programa in 'Nn':
        break

print('-≃'*30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
media = soma /len(dados)
print(f'B) A média de idade é de {media} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in dados:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('THE END!')

