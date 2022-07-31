lista = []
maior = 0
for v in range(0, 5):

    num = int(input('Digite um valor: '))
    if num >= maior: # verificar qual valor ficara no final da lista
        maior = num
        print('Adicionado no final da lista...')
        lista.append(num)

    else:
        if num < lista[0]: # verificando o primeiro numero apos o maior
            lista.insert(0, num)
            print('Valor adicionado na posiçao 0...')

        elif num > lista[0] and num < lista[1]:
            lista.insert(1, num)
            print('Valor adicionado na posiçao 1...')

        elif num > lista[1] and num < lista[2]:
            lista.insert(2, num)
            print('Valor adicionado na posiçao 2...')

        elif num > lista[2] and num < lista[3]:
            lista.insert(3, num)
            print('Valor adicionado na posiçao 3...')

print('-=' * 20)
print(f'Os numeros digitados em ordem foram: {lista}')