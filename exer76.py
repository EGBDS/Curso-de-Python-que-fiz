'''lista = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20',
         'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
print('{:<}{}R${:>7}'.format(lista[0], '.' * (31 - len(lista[0])), lista[1]))
print('{:<}{}R${:>7}'.format(lista[2], '.' * (31 - len(lista[2])), lista[3]))
print('{:<}{}R${:>7}'.format(lista[4], '.' * (31 - len(lista[4])), lista[5]))
print('{:<}{}R${:>7}'.format(lista[6], '.' * (31 - len(lista[6])), lista[7]))
print('{:<}{}R${:>7}'.format(lista[8], '.' * (31 - len(lista[8])), lista[9]))
print('{:<}{}R${:>7}'.format(lista[10], '.' * (31 - len(lista[10])), lista[11]))
print('{:<}{}R${:>7}'.format(lista[12], '.' * (31 - len(lista[12])), lista[13]))
print('{:<}{}R${:>7}'.format(lista[14], '.' * (31 - len(lista[14])), lista[15]))
print('{:<}{}R${:>7}'.format(lista[16], '.' * (31 - len(lista[16])), lista[17]))
print('-' * 40)'''

#OU

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
             'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8}')
print('-' * 40)
