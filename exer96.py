def multiplicador(a, b):
    multi = a * b
    print(f'A área de um terreno {a}x{b} é de {multi}m².')


print('  Controle de Terrenos')
print('-' * 30)
multiplicador(a=float(input('LARGURA (m): ')), b=float(input('COMPRIMENTO (m): ')))
