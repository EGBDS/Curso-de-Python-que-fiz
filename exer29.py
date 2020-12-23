v = float(input('Qual é a velocidade atual do carro? '))
if v<=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${:.2f}! \nTenha um bom dia! Dirija com segurança!'.format((v-80)*7))
