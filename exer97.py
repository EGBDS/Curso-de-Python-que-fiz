def frase(palavras):
    print('~' * len(palavras) + '~~')
    print(palavras)
    print('~' * len(palavras) + '~~')


frase(palavras='Gustavo Guanabara')
frase(palavras='Curso de Python no YouTube')
frase(palavras='CeV')
#MEU ACIMA
def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('Cev')
