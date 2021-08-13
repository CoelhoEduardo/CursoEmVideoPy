aluno = dict()
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] <= 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
print('-#'*30)
for n, m in aluno.items():
    print(f'- {n} = {m}')

