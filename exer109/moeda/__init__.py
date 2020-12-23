def moeda(p=0):
    p = f'R${p:.2f}'.replace('.', ',')
    return p


def aumentar(p=0, v=0, show=True):
    if show == True:
        por = (p / 100) * v
        result = p + por
        return f'R${result:.2f}'.replace('.', ',')
    else:
        por = (p / 100) * v
        result = p + por
        return result


def diminuir(p=0, v=0, show=True):
    if show == True:
        por = (p / 100) * v
        result = p - por
        return f'R${result:.2f}'.replace('.', ',')
    else:
        por = (p / 100) * v
        result = p - por
        return result


def dobro(p, show=True):
    if show == True:
        result = p * 2
        return f'R${result:.2f}'.replace('.', ',')
    else:
        result = p * 2
        return result


def metade(p, show=True):
    if show == True:
        result = p / 2
        return f'R${result:.2f}'.replace('.', ',')
    else:
        result = p / 2
        return result
