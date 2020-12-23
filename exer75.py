'''num = int(input('Digite um número: '))
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
nums = (num, num1, num2, num3)
print(f'Você digitou os valores {nums}')
print('O valor 9 apareceu {} vezes'.format(nums.count(9)))
for pos in enumerate(nums):
    if 3 in nums:
        print('O valor 3 apareceu na {}ª posição'.format(nums.index(3)+1))
    else:
        print('O valor 3 não foi digitado em nenhuma posicão')
    break
print('Os valores pares digitados foram', end=' ')
if num % 2 == 0:
    print(num, end=' ')
if num1 % 2 == 0:
    print(num1, end=' ')
if num2 % 2 == 0:
    print(num2, end=' ')
if num3 % 2 == 0:
    print(num3, end=' ')'''

#OU

núm = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posicão')
else:
    print('O valor 3 não foi digitado em nenhuma posicão')
print('Os valores pares digitados foram', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
