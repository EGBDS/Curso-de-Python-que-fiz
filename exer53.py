frase = str(input('Digite uma frase: ')).upper().strip()#strip tira os espaços da borda, o upper deixa as palavras em maiusculo
palavras = frase.split() #split gera uma lista
junto = ''.join(palavras) #juntou tudo em uma so palavra, uma so str
'''inverso = '''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1): #inverso da palavra# o len vai pegar o numero de letras do 'junto'
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é uma palíndromo!')
