pessoas = {'Nome': 'Eduardo', 'Sexo': 'M', 'Idade': 22}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-'*100)
pessoas['peso'] = 71.10
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*30)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['Sigla'])
print('-'*30)

estado = dict()
Brasil = list ()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()

