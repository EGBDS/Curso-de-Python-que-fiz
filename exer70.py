total = precoalto = maisbarato = contador = 0
produtomaisbarato = ''
print('-'*40)
print('{: ^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    contador += 1
    if contador == 1 or preco < maisbarato:
        maisbarato = preco
        produtomaisbarato = produto
    if preco > 1000:
        precoalto += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        break
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {precoalto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtomaisbarato} que custa R${maisbarato:.2f}')
