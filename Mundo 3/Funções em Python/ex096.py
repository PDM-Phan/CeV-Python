def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de {a}m2')


print(' Controle de terrenos ')
print('-' * 25)
area(l=float(input('LARGURA (m): ')), c=float(input('COMPRIMENTO (m): ')))
