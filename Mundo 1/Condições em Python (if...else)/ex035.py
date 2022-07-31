from termcolor import colored
from time import sleep
print(colored('-=-', 'yellow', attrs=['bold']) * 20)
print(colored('Voce quer saber se tres retas conseguem formar um triangulo? ', 'yellow', attrs=['bold']))
print(colored('-=-', 'yellow', attrs=['bold']) * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
print('ANALIZANDO AS RESTAS....')
sleep(3)
print('RESULTADO: ')
sleep(1)
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('{}, é possivel formar um triangulo.'.format(colored('SIM', 'cyan', attrs=['bold'])))
else:
    print('{} é possivel formar um triangulo com essas medidas.'.format(colored('NAO', 'red', attrs=['bold'])))
