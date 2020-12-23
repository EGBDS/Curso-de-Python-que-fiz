from time import sleep
n = int(input('Digite um número:'))
nu = n % 2
print('Analisando...')
sleep(4)
if nu == 0 :
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÌMPAR'.format(n))
