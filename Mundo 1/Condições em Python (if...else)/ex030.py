from termcolor import colored
num = int(input(colored('Digite um numero inteiro: ', 'magenta', attrs=['bold'])))
if num % 2 == 0:
    print('O numero {} é {}'.format(num, colored('PAR', 'blue', attrs=['bold'])))
else:
    print('O numero {} é {}.'.format(num, colored('IMPAR', 'blue', attrs=['bold'])))