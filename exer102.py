def fatorial(num, show=False):
    """
    -> Calcule o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    if show == False:
        for c in range(num, 0, -1):
            f *= c
        return f
    elif show == True:
        contador = 0
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if contador < num - 1:
                print(end=' x ')
                contador += 1
            else:
                print(end=' = ')
        for c in range(num, 0, -1):
            f *= c
        return f


print(fatorial(5, show=True))
help(fatorial)
