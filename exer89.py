ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
        if opc <= len(ficha) - 1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
'''MEU
boletim = [[], [], []]
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim[0].append(nome)
    boletim[1].append([nota1, nota2])
    boletim[2].append(media)
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao not in 'SN':
        print('NÃO RECONHEÇO ESSA OPÇÃO. Reinicie o programa!')
        break
    if opcao == 'N':
        break
print('-=' * 40)
print(f'{"No.":<}{"NOME":>5}{"MÉDIA":>20}')
print('-' * 30)
for c in range(0, len(boletim[0])):
    print('{:<}{:>8}{:>20}'.format(c, boletim[0][c], boletim[2][c]))
print('-' * 30)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    else:
        print(f'Notas de {boletim[0][opcao]} são {boletim[1][opcao]}')
print('FINALISANDO...')
print('<<< VOLTE SEMPRE >>>')'''
