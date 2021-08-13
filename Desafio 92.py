from datetime import date
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
anonascimento = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - anonascimento
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] > 0:
    trabalhador['Contrato'] = int(input('Ano de Contratação: '))
    trabalhador['Salario'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Contrato'] + 35 - anonascimento
print('≃'*30)
if trabalhador['CTPS'] != 0:
    print('DADOS DO TRABALHADOR')
else:
    print('DADOS DO CIDADÃO VAGABUNDO')
for t, d in trabalhador.items():
    print(f'- {t} = {d}')
