'''contador = sair = num1 = num = 0
while sair != 999:
    while num != 999:
        num1 += num
        contador += 1
        num = int(input('Digite um número [999 para parar]: '))
    else:
        contador += -1
        sair = 999
print('Você digitou {} números e a soma entre ele foi {}'.format(contador, num1))'''
#ou
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))