salário = float(input('Valor do salário: R$ '))
limite = 1250
aumento = (salário / 100) * 15
aumento2 = (salário / 100) * 10
if salário <= limite:
    print('O aumento do salário R${:.2f} foi de {}%, dando o valor final de R${:.2f}'.format(salário,15,salário+aumento))
else:
    print('O aumento do salário R${:.2f} foi de {}%, dando o valor final de R${:.2f}'.format(salário, 10,salário+aumento2))
