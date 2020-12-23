n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m =  (n1 + n2) / 2
print('Quem tirou {:.1f} e {:.1f} tem a média {:.1f}'.format(n1,n2,m))
if m <= 5.0:
    print('\033[31mREPROVADO\033[m')
elif m >= 5.0 and m <= 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
elif m >= 7.0:
    print('\033[32mAPROVADO\033[m')