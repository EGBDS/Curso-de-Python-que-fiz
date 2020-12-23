def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')

        else:
            return n


def leiafloat(msg2):
    while msg2 != float:
        r = input(msg2)
        try:
            r = float(r)
        except ValueError:
            print('\033[31mERRO! Digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return r


n = leiaint('Digite um inteiro: ')
r = leiafloat('Digite um Real: ')
print(f'Você acabou de digitar o número {n} e o real foi {r:.2f}')
