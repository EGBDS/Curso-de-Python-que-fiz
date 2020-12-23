'''from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
par = impar = contador = 0
while True:
    num = int(input('Diga um valor entre 0 e 10: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-'*40)
    computador = randint(0, 10)
    soma = num + computador
    par = soma % 2 == 0
    impar = soma % 2 == 1
    if par:
        print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU PAR')
        print('-'*40)
        if soma == par:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Vocè jogou {num} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('-'*40)
        if soma != par:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    print('=-'*20)
print('=-'*20)
print(f'GAME OVER! Você venceu {contador} vezes.')'''


