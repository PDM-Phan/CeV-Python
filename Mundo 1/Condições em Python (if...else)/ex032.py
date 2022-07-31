from termcolor import colored
from datetime import date
print('Esta querendo saber se um ano é bissexto? N TEM PROBLEMA SO LANSA NO PEITO DO PAI Q É GGWP!')
ano = int(input('DIZ AI O ANO PRA VER SE EU N DIGO Q É BISSEXTO! COLOQUE 0 PARA O ANO ATUAL! > '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(colored('É CLARO Q É!! BIRRLLLL!', 'cyan', attrs=['bold']))
else:
    print('{}, {} n é ano BISSEXTO'.format(colored('NOP', 'red', attrs=['bold']), ano))
