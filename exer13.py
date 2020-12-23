salario = float(input('Qual é o salário do fundionário? R$'))
novo = salario + (salario*15/100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario,novo))
