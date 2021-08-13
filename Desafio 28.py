import emoji
from random import randint
from time import sleep
print('JOGO DE ADIVINHAÇÃO')
print('-#-#-' * 20)
print('TENTE ADIVINHAR EM QUE NUMERO ESTOU PENSANDO DE 0 A 10')
print('-#-#-' * 20)
computador = randint(0,5)

jogador = int(input('Em qual numero estou pensando? '))
if jogador == computador:
    print(emoji.emojize('ACERTOU MIZERAVI :wink:', use_aliases=True))
    print(emoji.emojize('PARABENS, Voce ganhou :grimacing:', use_aliases=True))
else:
    print(emoji.emojize('EEEEEEEEROOOOOOOUU, TENTE NOVAMENTE :satisfied:', use_aliases=True))
    print(emoji.emojize('EU GANHEI MUAHAHAHAHAHA :smiling_imp:, eu pensei no {} e não no {}, fracassado'.format(computador, jogador), use_aliases=True))
print('waiting')
sleep(1)
print('END')

