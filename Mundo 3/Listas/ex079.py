lista = []
while True:

    num = int(input('Digite um valor: '))

    if lista.count(num) == 0: # se o valor digitado for unico
        lista.append(num) # sera adicionado à lista
        print('Valor adicionado com sucesso...')

    else: # se nao for unico
        print('Valor duplicado! Nao sendo adicionado...') # nao sera adicionado

    esc = ' '
    while esc not in 'NS':
        esc = input('Deseja continuar?[S/N] ').upper().strip()
    if esc == 'N':
        break

print('Programa finalizado.')
print(f'Os valores unicos que voce digitou em ordem crescente foram: {lista}')
lista.sort() # colocar os valores da lista em ordem crescente
print(f'Em ordem crescente ficara: {lista}')