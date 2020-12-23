'''comando
try: #tentar
    operacao
except: # se der problema
    falha
else: # se o 'try' der certo
    deu certo
finally: # acontece independente se deu certo/erro
    certo/falha'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre: Muito obrigado!')
