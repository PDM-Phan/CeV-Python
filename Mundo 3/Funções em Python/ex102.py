def fatorial(n, show=False):
    from time import sleep
    valor = 1
    while n >= 1: # cauculo de fatorial
        if show: # se show for true
            print(n, end='')
            sleep(0.5)
            print(' x ' if n > 1 else ' = ', end='')
        valor *= n
        n -= 1
    return valor


# Programa principal
n = int(input('Que numero voce quer ver? '))
show = input('Deseja mostrar o cauculo? [S/N] ').upper()
if show == 'S':
    show = True
else:
    show = False
print(fatorial(n, show))