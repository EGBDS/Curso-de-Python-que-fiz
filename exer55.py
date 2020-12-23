'''p1 = float(input('Peso da 1ª pessoa: '))
p2 = float(input('Peso da 2ª pessoa: '))
p3 = float(input('Peso da 3ª pessoa: '))
p4 = float(input('Peso da 4ª pessoa: '))
p5 = float(input('Peso da 5ª pessoa: '))
if p1 > p2 and p1 > p3 and p1 > p4 and p1 > p5:
    print('O maior peso lido foi de {}Kg'.format(p1))
elif p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5:
    print('O maior peso lido foi de {}Kg'.format(p2))
elif p3 > p1 and p3 > p2 and p3 > p4 and p3 > p5:
    print('O maior peso lido foi de {}Kg'.format(p3))
elif p4 > p1 and p4 > p2 and p4 > p3 and p4 > p5:
    print('O maior peso lido foi de {}Kg'.format(p4))
elif p5 > p1 and p5 > p2 and p5 > p3 and p5 > p4:
    print('O maior peso lido foi de {}Kg'.format(p5))
else:
    print('são todos iguais')
if p1 < p2 and p1 < p3 and p1 < p4 and p1 < p5:
    print('O menor peso lido foi de {}Kg'.format(p1))
elif p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5:
    print('O menor peso lido foi de {}Kg'.format(p2))
elif p3 < p1 and p3 < p2 and p3 < p4 and p3 < p5:
    print('O menor peso lido foi de {}Kg'.format(p3))
elif p4 < p1 and p4 < p2 and p4 < p3 and p4 < p5:
    print('O menor peso lido foi de {}Kg'.format(p4))
elif p5 < p1 and p5 < p2 and p5 < p3 and p5 < p4:
    print('O menor peso lido foi de {}Kg'.format(p5))'''
    #OU
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))