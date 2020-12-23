from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade, atual))
f = 18 - idade
p = idade - 18
if idade < 18:
    print('Você ainda não precisa se alistar ao serviço militar, ainda falta {} anos'.format(f))
elif idade == 18:
    print('Você precisa se alistar imediatamente ao serviço militar')
elif idade > 18:
    print('Você passou {} anos da idade do seu alistamento'.format(p))
