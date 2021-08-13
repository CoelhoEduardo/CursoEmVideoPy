'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
print('FEMININO = 1 / MASCULINO = 2')
sexo = int(input('Qual e o seu sexo ?: '))
feminino = 1
masculino = 2
if sexo == 1:
    print('Não há necessidade de fazer alistamento')
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O ano é {} e Você tem / irá fazer {} anos'.format(atual, idade))
if idade < 18:
    print('Você ainda vai se alistar')
    print('Faltam {} anos para você poder se alistar'.format(18 - idade))
    print('Seu alistamento será no ano de {}'.format(nascimento + 18))
elif idade == 18:
    print('Já é hora de se alistar')
elif idade > 18:
    print('VOCE JA DEVIA TER SE ALISTADO!!!!!!!')
    print('JA PASSARAM-SE {} ANOS DO PRAZO DE ALISTAMENTO TROUXAO'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nascimento + 18))


