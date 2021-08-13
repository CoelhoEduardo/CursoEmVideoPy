'''teste = list()
teste.append('Eduardo')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 24
galera.append(teste[:])
print(galera)'''

galera = [['Eduardo', 22], ['Mariana', 24], ['Yuri', 23], ['Isa', 21]]
print(galera[0][0], galera[1])

folks = list()
data = list()
totmai = totmen = 0
for c in range (0,3):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idade: ')))
    folks.append(data[:])
    data.clear()

for p in folks:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')

print(folks)