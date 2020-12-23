r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
    if r1 == r2 and r2 == r3: #ou if r1 == r2 == r3:
        print('O Triângulo que será formado é equilatero')
    elif r1 != r2 or r2 != r3 or r3 != r1: #ou elif r1 != r2 != r3 != r1:
        print('O Triângulo que será formado é isosceles')
    else:
        print('O Triângulo que será formado é escaleno')
else:
    print('As retas NÂO PODEM formar um triângulo')
