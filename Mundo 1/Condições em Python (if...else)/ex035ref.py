from termcolor import colored
from time import sleep
print(colored('-=-', 'yellow', attrs=['bold']) * 20)
print(colored('Voce quer saber se tres retas conseguem formar um triangulo? ', 'yellow', attrs=['bold']))
print(colored('-=-', 'yellow', attrs=['bold']) * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
print('ANALIZANDO AS RETAS....')
sleep(2)
print('RESULTADO: ')
sleep(1)
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Sim, é possiel formar um triangulo')
    if r1 == r2 == r3:
        print('E sera {}.'.format(colored('EQUILATERO', 'blue', attrs=['underline'])))
    elif r1 == r2 or r1 == r3 or r2 == r3 or r3 == r1:
        print('E sera {}.'.format(colored('ISÓCELES', 'blue', attrs=['underline'])))
    elif r1 != r2 != r3 != r1:
        print('E sera {}.'.format(colored('ESCALENO', 'blue', attrs=['bold'])))
else:
    print('{} é possivel formar um triangulo com essas medidas.'.format(colored('NAO', 'red', attrs=['underline'])))