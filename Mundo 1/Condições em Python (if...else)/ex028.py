import random
from time import sleep
from termcolor import colored
lola = random.randint(0, 5)
cor = '-=-' * 23
print(colored(cor, 'yellow', attrs=['bold']))
print(colored('Eu estou pensando em um numero, de 0-5, voce consegue adivinhar?', 'blue', attrs=['bold']))
print(colored(cor, 'yellow', attrs=['bold']))
sossa = int(input(colored('Que numero voce acha q eu estou pensando? ', 'blue', attrs=['bold'])))
print(colored('HMHMMM, CRIANDO EXPECTATIVA...', 'cyan', attrs=['bold']))
sleep(3)
if sossa == lola:
    print(colored('MEU SANTO ALÁ!, VOCE ACEERTOU!', 'green', attrs=['bold']))
else:
    print(colored('HAHAHAHAHAHAH TROUXA VOCE ERROU AHAHAHAHAHAHA!!', 'red', attrs=['bold']))