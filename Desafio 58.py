'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
palpw = 0
palp = 0
total = 0
print('JOGO DE ADIVINHA V2.0')
print('-='*22)
print('EM QUE NUMERO O PC ESTA PENSANDO DE 0 Á 10')
print('-='*22)
computador = randint(0,10)
#Minha resolucao
'''jogador = int(input('Escolha um numero: '))
while computador != jogador:
    print('ERROU. Tente novamente')
    jogador = int(input('Escolha um numero: '))
    palpw += 1
palp+=1
total = palp + palpw
print('Voce precisou de {} palpites para chegar no resultado'.format(total))
print('PARABENS, VOCE ACERTOU')'''
#resultado do professor
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palp += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente novamente')
print('Parabens, voce acertou. Precisou de {} palpites para chegar no numero'.format(palp))
