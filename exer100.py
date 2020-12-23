from random import randint
from time import sleep
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))


def sorteia(*nums):
    print('Sorteando 5 valores da lista: ', end='')
    for num in numeros:
        print(num, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(*nums):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia(numeros)
somapar(numeros)
