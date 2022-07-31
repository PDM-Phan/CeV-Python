import math
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
# h = pow(co, 2) + pow(ca, 2)
h = math.hypot(co, ca)
print('Com os valores de\n '
      '\033[4m{}\033[m para o cateto oposto e\n '
      '\033[4m{}\033[m para o cateto adjacente'.format(co, ca))
# print('O valor da hipotenusa é {:.2f}'.format(sqrt(h)))
print('O valor da hipotenusa é \033[4;32m{:.2f}\033[m'.format(h))
