valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao not in 'SN':
        print(f'Não reconheço o que você digitou "{opcao}". Reinicie o programa!')
        break
    if opcao == 'N':
        print('-=' * 40)
        break
print(f'Você digitou {len(valor)} elementos.')
print(f'Os valores em ordem decrescente são ', end='')
valor.sort(reverse=True)
print(valor)
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
