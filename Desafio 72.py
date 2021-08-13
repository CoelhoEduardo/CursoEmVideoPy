'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
programa = ''
contagem = ('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
            'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    leitor = int(input('Tecle um numero entre 0 e 20: '))
    while leitor > 20 or leitor < 0:
        leitor = int(input('Número Inválido. Tente novamente entre 0 e 20: '))
    print(f'Você digitou o número {contagem[leitor]}')

    programa = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if programa == 'N':
        break





