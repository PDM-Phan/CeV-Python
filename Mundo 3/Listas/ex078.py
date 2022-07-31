lista = []
for n in range(1, 6):

    lista.append(int(input(f'Digite um valor na posiçao {n}: '))) # adicionando valores a lista baseado no loop

print('-=' * 30)
print(f'Voce digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posiçoes ', end='') # o maior numero da lista
for p, na in enumerate(lista):
    if na == max(lista): # encontrando a posiçao do max na lista e printando sua posiçao
        print(f'{p + 1}...', end=' ')

print(f'\nO menor valor digitado foi {min(lista)} nas posiçoes ', end='') # o menor numero da lista
for p, na in enumerate(lista):
    if na == min(lista): # encontrando a posiçao do min na lista e printando sua posiçao
        print(f'{p + 1}...', end=' ')