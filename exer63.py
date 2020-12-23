print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
quantos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} {}'.format(t1, t2), end=' ')
count = 3
while count <= quantos:
    t3 = t2 + t1
    print('{}'.format(t3), end=' ')
    count += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
