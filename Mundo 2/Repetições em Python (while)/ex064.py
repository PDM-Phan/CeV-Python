n = 0
soma = 0 # soma dos valores
quantidade = 0 # quantidade de valores

while n != 999: # condiçao de parada
    n = int(input('Digite um numero interio: [999 para parar] '))
    if n != 999: # se a condiçao de parada nao for atingida
        soma += n # soma dos valores
        quantidade += 1 # quantidade de valores encontrados
# resultado
print('A soma de todos os {} numeros foi {}.'.format(quantidade, soma))