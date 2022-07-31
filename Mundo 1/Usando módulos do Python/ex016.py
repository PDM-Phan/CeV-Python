'''from math import floor
num = float(input('Digite qualquer numero real aqui > '))
print('O numero {} q voce digitou tem a parte inteira {}.'.format(num, floor(num)))'''

'''from math import trunc
num = float(input('Digite qualquer numero real aqui: '))
print('O numero {} q vc digitou tem a parte inteira de {}'.format(num, trunc(num)))'''

num = float(input('Digite qualquer numero real aqui: '))
print('O numero \033[1;34m{}\033[m q vc digitou tem a parte inteira de \033[1;36m{}\033[m'.format(num, int(num)))

