from random import shuffle
from termcolor import colored
print('\033[32mO mesmo professor quer sortear a ordem de apresentaçao de um grupo com esses participantes:\033[m')
n1 = input(colored('- ', 'white'))
n2 = input(colored('- ', 'white'))
n3 = input(colored('- ', 'white'))
n4 = input(colored('- ', 'white'))
grupo = [n1, n2, n3, n4]
shuffle(grupo)
# ngrupo = grupo
print('\033[32mApos o sorteio, a ordem de apresentaçao ficou:\033[m \033[31m{}\033[m'.format(', '.join(grupo)))
