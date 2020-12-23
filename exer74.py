from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in números: #tira as , e () da tupla 'números'
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(números)}') # o max mostra o maior valor dentro da ()
print(f'O menor valor sorteado foi {min(números)}') #o min mostrar o menor valor dentro da ()

