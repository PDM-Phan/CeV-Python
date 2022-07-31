from random import randint
from time import sleep

vitorias = 0
print('Vamos jogar PAR ou IMPAR!')
print('-=' * 20)
while True:
    computador = randint(0, 10) # escolha aleatoria do computador
    num = int(input('Digite um valor: ')) # escolha de numero do jogador
    jogador = str(input('Par ou Impar? [P/I] ')).upper().strip()
    while jogador not in 'PI':
        jogador = str(input('Par ou Impar? [P/I] ')).upper().strip()
    print('-' * 40)
    print('PAR!')
    sleep(1)
    print('OU!')
    sleep(1)
    print('IMPAR!')
    print('-' * 40)
    soma = computador + num # realizaçao da soma
    print('Voce jogou {} e o computador {}. total de {}'.format(num, computador, soma), end=' ')
    print('DEU PAR. ' if soma % 2 == 0 else 'DEU IMPAR.')
    if jogador == 'P': # se o jogador escolher par
        if soma % 2 == 0:
            print('-' * 40)
            print('VOCE VENCEU!')
            vitorias += 1 # adiciona uma vitora
            print('-=' * 20)
        else:
            print('-' * 40)
            print('VOCE PERDEU!')
            print('-=' * 20)
            break
    elif jogador == 'I': # se o jogador escolher impar
        if soma % 2 != 0:
            print('-' * 40)
            print('VOCE VENCEU!')
            vitorias += 1 # adiciona uma vitoria
            print('-=' * 20)
        else:
            print('-' * 40)
            print('VOCE PERDEU!')
            print('-=' * 20)
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Voce venceu {} vezes.'.format(vitorias)) # valor total das vitorias, caso haja alguma
