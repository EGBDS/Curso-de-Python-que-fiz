a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Analisando o menor número
menor = a
if a > b and b < c:
    menor = b
if b > c and b > a:
    menor = c
print('O menor valor é {}'.format(menor))
#Analisando o maior número
maior = a
if a < b and b > c:
    maior = b
if b < c and c > a:
    maior = c
print('O maior valor é {}'.format(maior))
