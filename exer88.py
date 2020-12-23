from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quntos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
'''MEU ABAIXAO
from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for c in range(1, quantidade + 1):
    print(f'Jogo {c}: [{randint(1, 60)}', end=', ')
    print(randint(1, 60), end=', ')
    print(randint(1, 60), end=', ')
    print(randint(1, 60), end=', ')
    print(randint(1, 60), end=', ')
    print(f'{randint(1, 60)}]', end='')
    print()
    sleep(2)
print('-=' * 5, '< Boa Sorte! >', '-=' * 5)'''
