dados = dict()
gols = []
total = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
for g in gols:
    dados['total'] = total = total + g
dados['gols'] = gols
print('-=' * 40)
print(dados)
print('-=' * 40)
print(f'O campo nome tem o valor {dados["nome"]}.')
print(f'O campo gols tem o valor {gols}.')
print(f'O campo total tem o valor {total}.')
print('-=' * 40)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for c, g in enumerate(gols):
    print(f'    => Na partida {c + 1}, fez {g} gols.')
print(f'Foi um total de {total} gols.')
