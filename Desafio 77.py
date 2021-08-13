palavras = ('PASSEIO','PASTEL','AMOR','INDIO','AFRICA',
            'ETIOPIA','BRASIL','PORTUGAL', 'BANANA',
            'FAZENDA','PYTHON','CURSO','EMVIDEO')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for vogais in p:
        if vogais.lower() in "aeiou":
            print(f'{vogais}', end=' ')

