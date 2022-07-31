'''import numpy as np
# pegando os pesos
pesos = []

for n in np.arange(1, 5):
    peso = float(input('Qual o peso da {} pessoa? '.format(n)))
    pesos.append(peso) # botando os dados na lista

pesos.sort(key=float) # colocando a lista em ordem crescente

print('O maior peso lido foi {} kg.'.format(pesos[-1]))
print('O menor peso lido foi {} kg.'.format(pesos[0]))'''

maior = 0 # maior inicial
menor = 0 # menor inicial

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    # 'O primeiro numero sera tanto o maior quanto o menor valor
    if p == 1:
        maior = peso
        menor = peso
    else:
        # se o peso for maior q a variavel 'maior', ent peso substituira
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} Kg'.format(maior))
print('O menor peso lido foi de {} Kg'.format(menor))
