import time
d = float(input('Qual a distância da viagem?'))
print('Analisando...')
time.sleep(4)
if d <= 200:
    print('A viagem custará R${:.2f}'.format(d*0.5))
else:
    print('A viagem custará R${:.2f}'.format(d*0.45))
