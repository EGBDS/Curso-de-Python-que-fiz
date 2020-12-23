def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    print(n)
    total = maior = menor = media = 0
    for v in n:
        total += 1
    r['total'] = total
    for v in n:
        if v == n[0]:
            maior = v
            menor = v
        else:
            if maior < v:
                maior = v
            if menor > v:
                menor = v
    r['maior'] = maior
    r['menor'] = menor
    for v in n:
        media += v
    media = media / len(n)
    r['média'] = media
    if sit == True:
        if media < 7:
            situacao = 'RUIM'
        else:
            situacao = 'BOA'
        r['situação'] = situacao
    return r


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
