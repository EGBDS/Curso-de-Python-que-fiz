n = int(input('Escolha um número para ver a sua tabuada: '))
for c in range(0, 11):
    ca = c * n
    print('{} x {} = {}'.format(n, c, ca))
