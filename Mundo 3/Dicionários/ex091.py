from random import randint
from time import sleep
# poderia ser usado para ordenar a lista pelos valores dos dados.
# from operator import itemgetter
total = [] # total de jogadas

for j in range(1, 5):
    jaaj = {}
    jaaj['Jogador'] = f'Jogador{j}'
    jaaj['Dado'] = randint(1, 6)
    total.append(jaaj.copy()) # criando uma copia dos valores do dicionario antes de reseta-lo

print('Valores sorteados: ')
for p in range(0, len(total)):
    print(f'    O {total[p]["Jogador"]} tirou {total[p]["Dado"]}')
    sleep(1)
# como tambem se pode usar a funçao lambda, oq eu prefiro
totalordem = sorted(total, key = lambda k: k['Dado'], reverse=True) # colocando a lista de dicionarios em ordem decrescente
# obs : a key = lambda retorna uma funçao k, q pode ser usada como padrao de ordem para a lista!!
print('Ranking dos Jogadores: ')
for o in range(0, len(totalordem)):
    print(f'    {o + 1}o. Lugar: {totalordem[o]["Jogador"]} com {totalordem[o]["Dado"]}')
    sleep(1)