from random import randint
from time import sleep

totten = 0 # total de tentativas
computador = randint(1, 10) # escolhar aleatoria do computador

print('Acabei de pensar em um numero de 1 - 10...')
jogador = int(input('Em que numero voce acha que eu estou pensando? '))

sleep(0.5)

while jogador != computador: # se o jogador errar
    totten += 1 # adcionar valor de tentativas
    if jogador < computador:
        print('Mais...', end=' ')
    if jogador > computador:
        print('Menos...', end=' ')
    print('Tente mais uma vez!!')
    jogador = int(input('Em que numero voce acha que eu estou pensando? ')) # outra tentativa
    if jogador == computador:
        break # atingiu a condiçao

if totten <= 2: # caso acerte com poucas tentativas
    print('PARABENS! voce so precisou de {} tentativas!'.format(totten))
else:
    print('Parabens voce acertou, mas...')
    print('Voce precisou de {} tentativas para acertar, mais sorte na proxima vez!'.format(totten))