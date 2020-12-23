num = int(input('Digite o número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print(' Unidade = {} \n Dezena = {} \n Centena = {} \n Milhar = {}'.format(u,d,c,m))
