import random
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
numerodocomputador = random.randint(0, 10)
numerodojogador = -1
quantastentativas = 0
print(numerodocomputador)
while numerodojogador != numerodocomputador:
    if numerodojogador != numerodocomputador:
        numerodojogador = int(input('Qual é o seu palpite? '))
        if numerodocomputador > numerodojogador:
            print('Mais... Tente mais uma vez.')
        elif numerodocomputador < numerodojogador:
            print('Menos... Tente mais uma vez.')
        quantastentativas +=1
else:
    print('Acertou com {} tentativas. Parabéns!'.format(quantastentativas))
