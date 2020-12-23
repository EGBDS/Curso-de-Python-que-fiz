informacoes = dict()
informacoes['Nome'] = str(input('Nome: '))
informacoes['media'] = float(input(f'Média de {informacoes["Nome"]}: '))
informacoes['Situação'] = 'Aprovado'
informacoes['Situação2'] = 'Recuperação'
print(f'- Nome é igual a {informacoes["Nome"]}')
print(f'- Média é igual a {informacoes["media"]}')
if informacoes['media'] >= 7:
    print(f'- Situação é igual a {informacoes["Situação"]}')
else:
    print(f'- Situação é igual a {informacoes["Situação2"]}')
