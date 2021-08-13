from time import sleep
alunos = []
dados = []
while True:
    dados.append(str(input('Nome do Aluno: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    programa = input('Deseja continuar ? [S/N] ')
    if programa in 'Nn':
        break
print('-'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for n, a in enumerate(alunos):
    print(f'{n:<4}{a[0]:<10}{(a[1]+a[2])/2:>8.1f}')
print('-'*30)
while True:
    print('-='*30)
    programa1 = int(input('Mostrar a nota de qual aluno ? (999 interrompe) '))
    if programa1 == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if programa1 <= len(alunos) -1:
        print(f'Notas de {alunos[programa1][0]}: N1 = {alunos[programa1][1]} N2 = {alunos[programa1][2]}')
print('PROGRAMA FINALIZADO.... VOLTE SEMPRE')

