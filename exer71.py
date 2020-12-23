#meu
'''cedula1 = 50
cedula2 = 20
cedula3 = 10
cedula4 = 1
contador1 = contador2 = contador3 = contador4 = 0
print('='*40)
print('{:^40}'.format('BANCO ECB'))
print('='*40)
while True:
    num = int(input('Quer valor você quer sacar? R$'))
    while cedula1 <= num:
        num = num - cedula1
        contador1 += 1
        if num <= 0:
            print(f'Total de {contador1} cédulas de R$50')
            break
    while cedula2 <= num:
        num = num - cedula2
        contador2 += 1
        if num <= 0:
            print(f'Total de {contador1} cédulas de R$50')
            print(f'Total de {contador2} cédulas de R$20')
            break
    while cedula3 <= num:
        num = num - cedula3
        contador3 += 1
        if num <= 0:
            print(f'Total de {contador1} cédulas de R$50')
            print(f'Total de {contador2} cédulas de R$20')
            print(f'Total de {contador3} cédulas de R$10')
            break
    while cedula4 <= num:
        num = num - cedula4
        contador4 += 1
        if num <= 0:
            print(f'Total de {contador1} cédulas de R$50')
            print(f'Total de {contador2} cédulas de R$20')
            print(f'Total de {contador3} cédulas de R$10')
            print(f'Total de {contador4} cédulas de R$1')
            break
    if num == 0:
        break
print('='*40)
print('Volte sempre ao BANCO ECB! Tenha um bom dia!')'''
#Correto
print('=' * 40)
print('{:^40}'.format('BANCO ECB'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -+ céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        if céd == 20:
            céd = 10
        if céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO ECB! Tenha um bom dia!')