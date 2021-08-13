''' Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''
soma = 0
maior = 0
sexo = ['M', 'F', 'm', 'f']
media = 0
nomev = ''
cont = 0
for p in range(1, 5):
    print('----{} PESSOA----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    soma += idade
    media = soma/4
    if idade < 20 and sexo in 'Ff':
        cont += 1
    if p == 1 and sexo in 'Mm':
        maior = idade
        nomev = nome
    if idade > maior and sexo in 'Mm':
        nomev = nome
        maior = idade
print('A media de idade do grupo é de {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomev, maior))
print('Tem {} meninas com menos de 20 anos no grupo'.format(cont))

