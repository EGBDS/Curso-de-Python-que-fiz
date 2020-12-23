import math
an = float(input('Digite o ângulo que você deseja:'))
seno =  math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(an,seno,an,cosseno,an,tangente))
