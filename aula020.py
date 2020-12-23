'''def mostralinha(): # def é uma função....
    print('_______________')


mostralinha()
print('      x        ')
mostralinha()
print('       y       ')
mostralinha()'''


'''def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
    
    
mensagem('SISTEMA DE ALUNOS')'''


'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)
soma(4, 1)'''


'''def contador(* num):
    for valor in num:
        print(f'{valor}', end=' ')
    tan = len(num)
    print('FIM')
    print(f'Recebi os valores {num} e são ao todo {tan} números')


contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)'''


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
