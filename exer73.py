times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlêtico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta','Atlético-GO')
print('-=' * 15)
print('lista de times do Brasileirão: {}'.format(times))
print('-=' * 15)
print('Os 5 primeiros são: {}'.format(times[0:5]))
print('-=' * 15)
print('Os 4 últimos são: {}'.format(times[-4:]))
print('-=' * 15)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('-=' * 15)
print('O Chapecoense está na {}ª posicão'.format(times.index('Chapecoense')+1))

