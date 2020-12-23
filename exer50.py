soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos números pares foi {}'.format(soma))
