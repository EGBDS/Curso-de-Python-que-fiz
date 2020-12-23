valor = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        print('Valor adicionado com sucesso...')
        valor.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        print('-=' * 20)
        break
print(f'Você digitou os valores {sorted(valor)}') # ou valor.sort()
