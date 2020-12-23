pessoascommaisde18 = quantidadedehomens = mulherescommenosde20 = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        pessoascommaisde18 += 1
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'F' and idade < 20:
        mulherescommenosde20 += 1
    if sexo == 'M':
        quantidadedehomens += 1
    print('-'*20)
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoascommaisde18}')
print(f'Ao todo temos {quantidadedehomens} homens cadastrados')
print(f'E temos {mulherescommenosde20} mulheres com menos de 20 anos')
