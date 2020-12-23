casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o salário do comprador? R$ '))
anos = float(input('Em quantos anos ele vai pagar? '))
prestações = casa / (anos * 12)
salário2 = salário * 30/100 #30% do salário
if prestações <= salário2:
    print('Parabéns! O seu empréstimo de R${:.2f}, com o calor mensal de R${:.2f}, será \033[32mAPROVADO\033[m!'.format(casa,salário2))
else:
    print('O seu empréstimo de R${:.2f}, \033[31mNÂO FOI APROVADO\033[m!'.format(casa))
