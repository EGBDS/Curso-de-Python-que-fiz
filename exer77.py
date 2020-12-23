palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras: #analisa cada palavra
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p: #analisa cada letra na palavra
        if letra in 'aeiou': #analisa se a letra está em 'aeiou'
            print(letra, end=' ')
