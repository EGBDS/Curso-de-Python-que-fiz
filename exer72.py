números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0:                                         #Ou if 0 <= num <= 20:
        print('Tente novamente.', end=' ')
    elif num > 20:
        print('Tente novamente.', end=' ')
    else:
        break
print(f'Você digitou o número {números[num]}')
