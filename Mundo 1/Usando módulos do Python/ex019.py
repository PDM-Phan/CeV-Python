from random import choice
from termcolor import colored
print('\033[32mUm professor quer escolher um aluno para apagar os quadros, seus nomes são:\033[m ')
n1 = input(colored('- ', 'white'))
n2 = input(colored('- ', 'white'))
n3 = input(colored('- ', 'white'))
n4 = input(colored('- ', 'white'))
alunos = [n1, n2, n3, n4]
e = choice(alunos)
print('\033[32mApós escolher aleatoriamente entre os nomes dos alunos, o escolhido foi:\033[m \033[91m{}\033[m'.format(e))
