valores = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1 } valor: '))
    if valor % 2 == 0:
        valores[0].insert(0, valor)
    else:
        valores[1].insert(1, valor)
print('-=' * 40)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
