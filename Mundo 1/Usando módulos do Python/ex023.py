from time import sleep
a = int(input('\033[93mDigite um numero de ATÉ 4 digitos\033[m: '))
'''casas = ['milhar:', 'centena:', 'dezena:', 'unidade:']
for c in range(1, len(a)+1):
   | print(casas[-c], a[-c])'''
print('\033[93mAnalizando o numero \033[1;32m{}\033[m...'.format(a))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 % 10
sleep(1)
print('- Unidade: \033[1;32m{}\033[m'.format(u))
print('- Dezena:  \033[1;32m{}\033[m'.format(d))
print('- Centena: \033[1;32m{}\033[m'.format(c))
print('- Milhar:  \033[1;32m{}\033[m'.format(m))
