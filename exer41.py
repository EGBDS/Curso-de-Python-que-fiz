from datetime import date
a = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - a
print('Quem nasceu em {} tem {} anos.'.format(a,idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14 and idade > 9:
    print('Classificação: INFANTIL')
elif idade <= 19 and idade > 14:
    print('Classificação: JUNIOR')
elif idade <= 20 and idade > 19:
    print('Classificação: SÊNIOR')
elif idade > 20:
    print('Classificação: MASTER')