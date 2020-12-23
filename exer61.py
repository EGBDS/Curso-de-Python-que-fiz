print('Gerador de PA')
print('-='*10)
primeirotermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeirotermo+razao
while cont != 10:
    print('{} '.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')
