def moeda(p=0):
    p = f'R${p:.2f}'.replace('.', ',')
    return p


def aumentar(p=0, v=0):
    por = (p / 100) * v
    return p + por


def diminuir(p=0, v=0):
    por = (p / 100) * v
    return p - por


def dobro(p):
    return p * 2


def metade(p):
    return p / 2

