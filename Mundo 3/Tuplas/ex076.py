produtos = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
print('-' * 40)
print(f'{" LISTA DE PRODUTOS ":^40}')
print('-' * 40)
for pos in range(0, len(produtos)): # ultilizar a posiçao dos valores
    if pos % 2 == 0: # produtos nas posiçoes pares
        print(f'{produtos[pos]:.<30}', end='')
    else: # valores nas posiçoes impas
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)