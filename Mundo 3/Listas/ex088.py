from random import randint
from time import sleep

jogostotais = [] # jogos totais
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
cont = 0 # contador de jogos
print(f'{f">>> SORTEANDO {jogos} JOGOS <<<":^30}')

while cont < jogos:
    jogo = []
    while len(jogo) != 6:
        valor = randint(1, 60)
        if jogo.count(valor) == 0:
            jogo.append(valor) # adicionando os valores a lista
    jogostotais.append(jogo[:]) # adicionando uma copia da lista nos jogos totais
    cont += 1 # adicionando a contador de jogos
print('-=' * 18)

for l in range(0, len(jogostotais)):
    jogostotais[l].sort() # colocando cada lista em ordem crescente
    print(f'Jogo {l + 1}: {jogostotais[l]}')
    sleep(1)
print('-=' * 18)
