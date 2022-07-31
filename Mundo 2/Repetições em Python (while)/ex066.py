soma = 0 # soma entre eles
cont = 0 # quantidade de numeros

while True:
    n = int(input('Digite um numero inteiro: [999 para encerrar] '))
    if n == 999: # condiçao para parada
        break # encerrar loop
    else:
        soma += n
        cont += 1

print('A quantidade de numero digitados foi {} \nE a sua soma é {}.'.format(cont, soma))
