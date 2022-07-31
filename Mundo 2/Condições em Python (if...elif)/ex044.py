from random import randint
from time import sleep
comch = ('\033[1;37mPEDRA\033[m', '\033[97mPAPEL\033[m', '\033[1;31mTESOURA\033[m')
computador = randint(0, 2)
print('''VOCE QUER JGOAR JOKENPO CONTRA MIM??!
ESCOLHA A SUA \033[93mARMA\033[m:
0 - \033[1;37mPEDRA\033[m 
1 - \033[97mPAPEL\033[m 
3 - \033[1;31mTESOURA\033[m''')
esc = int(input('QUAL SUA \033[93mARMA\033[m?! '))
print('\033[1;37mJO\033[m')
sleep(1)
print('\033[97mKEN\033[m')
sleep(1)
print('\033[1;31mPO\033[m!!!')
print('\033[1;33m-\033[m\033[1;31m=\033[m' * 14)
print('O COMPUTADOR JOGOU {}!!'.format(comch[computador]))
print('VOCE JOGOU {}!!'.format(comch[esc]))
print('\033[1;33m-\033[m\033[1;31m=\033[m' * 14)
# resultado:
if computador == 0: # computador usa pedra
    if esc == 0:
        print('Tsk, foi \033[33mEMPATE\033[m.')
    elif esc == 1:
        print('BOA JOGADA, voce \033[1;32mGANHOU!\033[m')
    elif esc == 2:
        print('RÁ, VOCE \033[91mPERDEU\033[m E EU \033[1;32mGANHEI!!\033[m')
elif computador == 1: # computador usou papel
    if esc == 0:
        print('RÁ, VOCE \033[91mPERDEU\033[m E EU \033[92mGANHEI!!\033[m')
    elif esc == 1:
        print('Tsk, foi \033[33mEMPATE\033[m.')
    elif esc == 2:
        print('BOA JOGADA, voce \033[1;32mGANHOU!\033[m')
elif computador == 2: # computador usou tesoura
    if esc == 0:
        print('BOA JOGADA, voce \033[1;32mGANHOU!\033[m')
    elif esc == 1:
        print('RÁ, VOCE \033[91mPERDEU\033[m E EU \033[92mGANHEI!!\033[m')
    elif esc == 2:
        print('Tsk, foi \033[33mEMPATE\033[m.')
