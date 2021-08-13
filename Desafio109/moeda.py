def aumentar(a=0, b=0, form=False):
    aumento = a + (a * b / 100)
    return aumento if form is False else moeda(aumento)


def diminuir(a=0, b=0, form=False):
    diminui = a - (a * b / 100)
    return diminui if form is False else moeda(diminui)


def dobro(a=0, form=False):
    dobrar = a * 2
    return dobrar if form is False else moeda(dobrar)


def metade(a=0, form=False):
    met = a / 2
    return met if form is False else moeda(met)


def moeda(a=0, cifrao='R$'):
    formatacao = f"{cifrao}{a:>.2f}".replace(".", ",")
    return formatacao
