cores = {'limpa':'\033[m',
        'vermelho':'\033[31m',
        'amarelo':'\033[33m',
        'roxo':'\033[35m',
        'preto e branco':'\033[7;30m',
        'verde':'\033[32m'}
efeito = '-=-' * 20
print('{}{}{}'.format(cores['vermelho'],efeito,cores['limpa']))
print('{}Analisador de Triângulos...{}'.format(cores['preto e branco'],cores['limpa']))
print('{}{}{}'.format(cores['vermelho'],efeito,cores['limpa']))
r1 = float(input('{}Primeiro segmento: {}'.format(cores['vermelho'],cores['limpa'])))
r2 = float(input('{}Segundo segmento: {}'.format(cores['amarelo'],cores['limpa'])))
r3 = float(input('{}Terceiro segmento: {}'.format(cores['roxo'],cores['limpa'])))
if r1 < r2 + r3:
    if r2 < r1 + r3:
        if r3 < r1 + r2:
            print('Os segmentos acima {}PODEM FORMAR{} triângulos!'.format(cores['verde'],cores['limpa']))
else:
    print('Os segmentos acima {}NÂO PODEM FORMAR{} triângulos!'.format(cores['vermelho'],cores['limpa']))
