from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
n = int(input('Vou pensar em um número entre 0 e 5.Tente advinhar:'))
print('-=-'*20)
print('Analisando...')
sleep(4)
if n==computador:
    print('Parabéns, o número escolhido pela máquina é {},foi igual ao seu número {}'.format(computador,n))
else:
    print('O número escolhido pela máquinha é {},e é diferente do escolhido por você {}'.format(computador,n))
