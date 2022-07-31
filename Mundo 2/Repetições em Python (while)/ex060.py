from time import sleep

n = int(input('Digite um numero para saber o seu fatorial: '))
print('Cauculando {}! = '.format(n), end='')
f = 1
sleep(0.5)

while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    sleep(0.5)
    f *= n
    n -= 1
print('{}'.format(f))
print('Fatoraçao completa.')

