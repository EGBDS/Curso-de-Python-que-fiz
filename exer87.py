matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0  #spar = soma dos pares, scol = soma da coluna
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da sgunda linha é {mai}.')
'''#MEU ABAIXO
somapares = 0
impares = []
maiorlinha2 = 0
linha = [int(input('Digite um valor para [0, 0]: ')), int(input('Digite um valor para [0, 1]: ')),
         int(input('Digite um valor para [0, 2]: '))]
linha2 = [int(input('Digite um valor para [1, 0]: ')), int(input('Digite um valor para [1, 1]: ')),
          int(input('Digite um valor para [1, 2]: '))]
linha3 = [int(input('Digite um valor para [2, 0]: ')), int(input('Digite um valor para [2, 1]: ')),
          int(input('Digite um valor para [2, 2]: '))]
print('-=' * 40)
print('[', linha[0], ']', '[', linha[1], ']', '[', linha[2], ']')
print('[', linha2[0], ']', '[', linha2[1], ']', '[', linha2[2], ']')
print('[', linha3[0], ']', '[', linha3[1], ']', '[', linha3[2], ']')
print('-=' * 40)
for v in linha:
    if v % 2 == 0:
        somapares = somapares + v
for v in linha2:
    if v % 2 == 0:
        somapares = somapares + v
for v in linha3:
    if v % 2 == 0:
        somapares = somapares + v
somaterceiracoluna = linha[2] + linha2[2] + linha3[2]
print(f'A soma dos valores pares é {somapares}.')
print(f'A soma dos valores da terceira colune é {somaterceiracoluna}.')
print(f'o maior valor da segunda linha é {max(linha2)}.')'''
