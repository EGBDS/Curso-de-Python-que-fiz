print('{:=^40}'.format('LOJAS ECB'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('opção? '))
if opção == 1:
    print('O valor da sua compra R${:.2f} receberá 10% de desconto, ficando em R${:.2f} para ser pago.'.format(preço,preço * 10 /100))
elif opção == 2:
    print('O valor da sua compra R${:.2f} receberá 5% de desconto, ficando em R${:.2f} para ser pago.'.format(preço,preço * 5 /100))
elif opção == 3:
    print('O valor da sua compra R${:.2f} não receberá nenhum desconto.'.format(preço))
elif opção == 4:
    print('O valor da sua compra R${:.2f} receberá o juros de 20%, ficando em R${:.2f} para ser pago'.format(preço,(preço / 100) * 20 + preço))
else:
    print('\033[31mOPÇÃO INVÁLIDA\033[m de forma de pagamento, tente novamente.')