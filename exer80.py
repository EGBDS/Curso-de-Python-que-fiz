valores = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos <= len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')

#meu abaixo

valores = []
num = int(input('Digite um valor: '))
valores.insert(4, num)
print('Adicionado ao final da lista...')
num1 = int(input('Digite um valor: '))
if num > num1:
    valores.insert(0, num1)
    print('Adicionado na posição 0 da lista...')
else:
    valores.insert(4, num1)
    print('Adicionado no final da lista...')
num2 = int(input('Digite um valor: '))
if num > num2 < num1:
    valores.insert(0, num1)
    print('Adicionado na posição 0 da lista...')
elif num > num2 > num1:
    valores.insert(1, num2)
    print('Adicionado na posição 1 da lista...')
else:
    valores.insert(4, num2)
    print('Adicionado ao final da lista...')
num3 = int(input('Digite um valor: '))
if num > num3 < num1 and num3 < num2:
    valores.insert(0, num3)
    print('Adicionado na posição 0 da lista...')
elif num < num3 > num1 and num3 > num2:
    valores.insert(4, num3)
    print('Adicionado ao final da lista...')
elif num < num3 < num1 and num3 < num2:
    valores.insert(1, num3)
    print('Adicionado na posição 1 da lista...')
else:
    valores.insert(2, num3)
    print('Adicionado na posição 2 da lista...')
num4 = int(input('Digite um valor: '))
if num > num4 < num1 and num2 > num4 < num3:
    valores.insert(0, num4)
    print('Adicionado na posição 0 da lista...')
elif num < num4 > num1 and num2 < num4 > num3:
    valores.insert(4, num4)
    print('Adicionado ao final da lista...')
elif num > num4 > num1 and num2 > num4 < num3:
    valores.insert(1, num4)
    print('Adicionado na posição 1 da lista...')
elif num > num4 < num1 and num2 > num4 < num3:
    valores.insert(2, num4)
    print('Adicionado na posição 2 da lista...')
elif num > num4 > num1 and num2 < num4 > num3:
    valores.insert(3, num4)
    print('Adicionado na posição 3 da lista...')
print('-=' * 20)
print(f'Os valores digitados em ordem foram {valores}')
