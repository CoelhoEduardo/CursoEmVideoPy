


def notas(*n, sit=False):
    """
    :param n: Uma ou mais notas dos alunos (aceita variaveis)
    :param sit: Situação do Aluno dependendo da nota (opcional)
    :return: retorna o valor do dicionario das notas
    """
    import emoji
    r = dict()
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = emoji.emojize('Boa :heart:', use_aliases=True)
        elif r['média'] >= 5:
            r['situação'] = emoji.emojize('Razoável :smile:', use_aliases=True)
        else:
            r['situação'] = emoji.emojize('RUIM!! :worried:', use_aliases=True)

    return r

#programa Principal
resp = notas(6, 6.5, 7.5, sit=True)
print(resp)
