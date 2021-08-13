def aumentar(a=0, b=0):
    aumento = a + (a * b / 100)
    return aumento


def diminuir(a=0, b=0):
    diminui = a - (a * b / 100)
    return diminui


def dobro(a=0):
    dobrar = a * 2
    return dobrar


def metade(a=0):
    met = a / 2
    return met


def moeda(a=0, cifrao='R$'):
    formatacao = f"{cifrao}{a:>.2f}".replace(".", ",")
    return formatacao



