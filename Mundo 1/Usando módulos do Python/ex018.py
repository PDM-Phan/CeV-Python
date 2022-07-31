#cauculando o seno coseno e a tangente de um angulo
import math
a = float(input('\033[1;95mDigite um angulo qualquer\033[m: '))
# print(f'Dado o angulo, \nseu seno é {math.sin(a)} \nseu cosseno é {math.cos(a)} \ne sua a tangente {math.tan(a)}')
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('\033[1;95mDado o angulo\033[m, \033[4m{}\033[m, \n'
      '\033[1;95mseu seno é\033[m \033[4m{:.2}\033[m,\n'
      '\033[1;95mseu coseno\033[m \033[4m{:.2}\033[m, \n'
      '\033[1;95me sua tangente é\033[m \033[4m{:.2}\033[m.'.format(a, s, c, t))
