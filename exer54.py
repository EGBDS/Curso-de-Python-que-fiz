import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8, 1):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual - ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
