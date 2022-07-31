from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('\033[93mEscolha uma das opçoes abaixo para\033[m:')
print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR NUMERO
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR''')
es = int(input('\033[93m>>>> Qual opçao voce deseja?\033[m '))

while es != 5: # enquanto nao seja a opçao 5

    if es == 1: # caso for opçao 1
        som = n1 + n2
        print('A soma dos numeros {} e {} sera {}.'.format(n1, n2, som))
        print('\033[93m=-=\033[m' * 15)
        sleep(1)
        print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR NUMERO\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR''')
        es = int(input('\033[93m>>>> Qual outra opçao voce deseja?\033[m ')) # selecionar uma nova opçao

    elif es == 2: # caso for a opçao 2
        mult = n1 * n2
        print('A multiplaçao dos numeros {} e {} sera {}.'.format(n1, n2, mult))
        print('\033[93m=-=\033[m' * 15)
        sleep(1)
        print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR NUMERO\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR''')
        es = int(input('\033[93m>>>> Qual outra opçao voce deseja?\033[m ')) # selecionar uma nova opçao

    elif es == 3: # caso for a opçao 3
        if n2 > n1:
            print('Entre {} e {} o maior numero é {}.'.format(n1, n2, n2))
        elif n1 > n2:
            print('Entre {} e {} o maior numero é {}.'.format(n1, n2, n1))
        elif n1 == n2:
            print('Nao ha numero maior, pois ambos sao IGUAIS.')
        print('\033[93m=-=\033[m' * 15)
        sleep(1)
        print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR NUMERO\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR''')
        es = int(input('\033[93m>>>> Qual outra opçao voce deseja?\033[m ')) # selecionar uma nova opçao

    elif es == 4: # caso for a opçao 4
        n1 = int(input('Qual sera o novo numero? '))
        n2 = int(input('Qual sera o outro novo valor? '))
        print('\033[93m=-=\033[m' * 15)
        sleep(1)
        print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR NUMERO\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR''')
        es = int(input('\033[93m>>>> Qual outra opçao voce deseja?\033[m ')) # selecionar uma nova opçao
    else: # caso digite qualquer coisa alem do pedido
        print('Opçao invalida. Tente novamente...')
        print('\033[93m=-=\033[m' * 15)
        sleep(1)
        print('''[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR NUMERO\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR''')
        es = int(input('\033[93m>>>> Qual outra opçao voce deseja?\033[m '))  # selecionar uma nova opçao

print('\033[95mAte a proxima vez!\033[m')
