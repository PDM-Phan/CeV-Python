from time import sleep
from random import randint
valores = []


def sortear(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        sleep(0.5)
        lista.append(num)
    print('PRONTO!')


def somapar(lista):
    print('Somando os valores pares de ', end='')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'{lista}, temos {soma}')


# Programa principal
sortear(valores)
somapar(valores)