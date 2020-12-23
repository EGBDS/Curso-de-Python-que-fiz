valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao not in 'SN':
        print('Não reconheço essa função.... Reinicie o programa!')
        break
    if opcao == 'N':
        break
print('=' * 40)
print(f'A lista completa é {valores}')
pares = []
impares = []
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
