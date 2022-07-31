from time import sleep


def maior(*val):
    print('-=' * 30)
    print('Analizando os valores passados... ')
    for c in val: # print cada valor da lista
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(val)} valores ao todo.')
    if len(val) == 0: # caso nao ha valor informado 
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(val)}.')
    sleep(1)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
