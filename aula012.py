'''if:
    bloco1
elif:
    bloco2
elif:
    bloco3
else:
    bloco4'''
nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome in 'Erick João Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome == 'Rosa':
    print('Belo nome você tem!')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, {}!'.format(nome))