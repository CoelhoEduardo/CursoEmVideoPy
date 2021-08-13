def voto(ano):
    from datetime import date
    print('-'*50)
    atual = date.today().year
    idade = atual - ano
    if 60 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'


nascimento = int(input('Ano de Nascimento: '))
print(voto(nascimento))

