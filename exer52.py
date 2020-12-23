num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1, 1):
    if num % c == 0:
        print('\033[32m{}\033[m'.format(c))
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(c))
print('O número {} e divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('O número {} é PRIMO!'.format(num))
else:
    print('O número {} NÂO É PRIMO!'.format(num))