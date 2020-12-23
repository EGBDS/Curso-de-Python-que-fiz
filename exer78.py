valores = []
menor = 0
maior = 0
print('-=' * 40)
print(f'Os valores digitados são {valores}')
print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
       if v == maior:
              print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
       if v == menor:
              print(f'{i}...', end='')
print()
