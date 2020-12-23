from datetime import date


def voto(num=0):
    idade = date.today().year - num
    if 16 <= idade < 18:
        a = f'Com {idade} anos: VOTO OPCIONAL.'
        return a
    elif 18 <= idade <= 64:
        a = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
        return a
    elif idade < 16:
        a = f'Com {idade} anos: NÃO VOTA.'
        return a
    else:
        a = f'Com {idade} anos: VOTO OPCIONAL.'
        return a


print('-' * 30)
n = voto(int(input('Em que ano você nasceu? ')))
print(n)



