from time import sleep


def contador(i, f, p):
    if p < 0: # se p for escrito de forma negativa
        p *= -1
    elif p == 0: # se p for 0
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i > f: # se o incio for maior que o fim, entao p é negativo
        p = -p
    while i != f + p: # enquanto o incio for diferente do fim, ira printar cada valor
        print(i, end=' ')
        i += p
        sleep(0.5)
    print('.')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a ontagem!')
contador(i=int(input('Inicio: ')), f=int(input('Fim: ')), p=int(input('Passo: ')))
