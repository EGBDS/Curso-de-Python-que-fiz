''' aposenta 35 anos de colaboracao/contribuicao
ctps carteira de trabalho '''
import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de Nascimento: '))
idade = datetime.date.today().year - dados['idade']
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps == 0:
    print('-=' * 40)
    print(f'- nome tem valor {dados["nome"]}')
    print(f'- idade tem o valor {idade}')
    print(f'- ctps tem o valor {ctps}')
else:
    dados['ctps'] = ctps
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['contratação'] - dados['idade'] + 35
    dados['salário'] = int(input('Salário: R$ '))
    print('-=' * 40)
    print(f'- nome tem o valor {dados["nome"]}')
    print(f'- idade tem o valor {idade}')
    print(f'- ctps tem o valor {dados["ctps"]}')
    print(f'- contratação tem o valor {dados["contratação"]}')
    print(f'- salário tem o valor {dados["salário"]:.1f}')
    print(f'- aposentadoria tem o valor {dados["aposentadoria"]}')
