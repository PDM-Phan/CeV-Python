lista = []
while True:

    num = int(input('Digite um valor: '))
    lista.append(num)
    esc = ' '

    while esc not in 'NS':
        esc = input('Deseja continuar?[S/N] ').upper().strip()
    if esc == 'N':
        break

print('-=' * 20)
print(f'Voce digitou {len(lista)} elementos.') # quantidade de elementos na lista
lista.sort(reverse=True) # lista organizada em ordem decrescente
print(f'Os valores digitados em ordem decrescente sao: {lista}')

if lista.count(5) == 0: # verificando se o valor 5 faz parte da lista
    print('O valor 5 nao faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')