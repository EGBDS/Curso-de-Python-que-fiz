'''#interactive help
help(print)
#ou
print(input.__doc__)'''
'''#docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada para teste
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)'''
'''#Parametro opcional
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')

 
somar(5, 6, 9)
somar(1, 4)
somar(7)'''
'''#Escopo de Variáveis
def teste(b):
    global a #essa função faz o A global perder o número e o A local se torna o A global
    a = 8 # A local
    b += 4 #escopo local
    c = 2 #escopo local
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # escopo global; A global
teste(a)
print(f'A fora vale {a}')'''
'''#Retornando Valores.... return
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
# ou
resposta = somar(3, 2, 5)
# ou
print(somar(3, 2, 5))'''
#exemplo
'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('não é par!')

#outro exemplo'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
