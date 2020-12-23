'''resposta = contador = media = maior = menor = dividido = 0
while resposta != 'N':
    contador += 1
    numero = int(input('Digite um número: '))
    if maior > numero:
        maior = maior
    else:
        maior = numero
    if contador < 2:
        menor = maior
    elif menor < numero:
        menor = menor
    else:
        menor = numero
    if contador > 1:
        media += numero
    else:
        media += numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
if resposta == 'N':
    resposta = 'N'
    dividido = contador
    if contador > 1:
        media = media / dividido
print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))'''
#OU
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Vocè digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))