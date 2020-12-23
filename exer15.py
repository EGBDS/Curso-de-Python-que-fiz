dias = int(input('Quantos dias alugados?'))
Km = int(input('Quantos Km rodados?'))
dia = dias*60
kmrodado = Km*0.15
print('O total a pagar é R${}'.format(dia+kmrodado))
