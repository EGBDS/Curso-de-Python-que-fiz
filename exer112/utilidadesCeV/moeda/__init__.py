from exer112.utilidadesCeV import dado


def resumo(p=0, a=0, b=0):

    aumento = (p / 100) * a + p
    aumento = f'R${aumento:.2f}'.replace('.', ',')
    reducao = (p/100) * b
    resultdimi = p - reducao
    resultdimi = f'R${resultdimi:.2f}'.replace('.', ',')
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(p)}')
    print(f'{"Dobro do preço:":<20}{dobro(p)}')
    print(f'{"Metade do preço:":<20}{metade(p)}')
    print(f'{"80% de aumento:":<20}{aumento}')
    print(f'{"35% de redução:":<20}{resultdimi}')
    print('-' * 30)


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
