sair = 1
primeirovalor = int(input('Primeiro valor: '))
segundovalor = int(input('Segundo valor: '))
while sair != 0:
    if sair != 0:
        sair = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n'
                         '[ 5 ] sair do programa\n>>>>> Qual é a sua opção? '))
        if sair == 1:
            print('{} + {} = {}'.format(primeirovalor, segundovalor, primeirovalor+segundovalor))
        elif sair == 2:
            print('{} x {} = {}'.format(primeirovalor, segundovalor, primeirovalor*segundovalor))
        elif sair == 3:
            if primeirovalor > segundovalor:
                print('O maior valor entre {} e {} é {}'.format(primeirovalor, segundovalor, primeirovalor))
            else:
                print('O maior valor entre {} e {} é {}'.format(primeirovalor, segundovalor, segundovalor))
        elif sair == 4:
            primeirovalor = int(input('Primeiro valor: '))
            segundovalor = int(input('Segundo valor: '))
        elif sair == 5:
            sair = 0
        elif sair != (0, 1, 2, 3, 4, 5):
            print('A sua opção não foi encontrada! Tente novamente.')
print('O programa está sendo fechado...')
