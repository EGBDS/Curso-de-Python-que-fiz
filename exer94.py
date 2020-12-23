dadosgerais = []
media = 0
mulheres = []
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    dadosgerais.append(dados)
    del dados
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print('-=' * 40)
print(f'- O grupo tem {len(dadosgerais)} pessoas.')
print(f'- A média de idade é de {media/len(dadosgerais):.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for c in dadosgerais:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
print()
for c in dadosgerais:
    if c['idade'] >= media/len(dadosgerais):
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
        print()
print('<< ENCERRADO >>')
