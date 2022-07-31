from time import sleep

while True:
    num = int(input('Tabuadad de \033[92m(Digite um numero negativo para parar)\033[m: ')) # valor da tabuada
    print('-=' * 15)
    sleep(1)
    if num < 0: # condiçao de parada
        break
    for t in range(1, 11): # tabuada
        total = num * t
        print('{} x {} = {}'.format(num, t, total))
    print('-=' * 15)
    sleep(1)

if num < 0: # mensagem printada apos fim do loop
    print('Voce digitou um numero \033[91mnegativo.\033[m')
    sleep(0.5)
    print('\033[91mTabuada encerrada.\033[m')
