preco = float(input('Qual e o preco do produto? R$'))
por = preco - (preco*5/100)

print('O produto que custava R${}, na promocao com desconto de 5% vai custar R${:.2f}'.format(preco,por))
