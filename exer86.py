matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        print()
'''#MEU ABAIXO'''
linha = [[int(input('Digite um valor para [0, 0]: '))], [int(input('Digite um valor para [0, 1]: '))],
         [int(input('Digite um valor para [0, 2]: '))],
         [int(input('Digite um valor para [1, 0]: '))], [int(input('Digite um valor para [1, 1]: '))],
         [int(input('Digite um valor para [1, 2]: '))],
         [int(input('Digite um valor para [2, 0]: '))], [int(input('Digite um valor para [2, 1]: '))],
         [int(input('Digite um valor para [2, 2]: '))]]
print('-=' * 40)
print(linha[0], linha[1], linha[2])
print(linha[3], linha[4], linha[5])
print(linha[6], linha[7], linha[8])
