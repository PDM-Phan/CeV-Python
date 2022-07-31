jogador = {} # perfil do jogador
gols = [] # lista com todos os gols
sgols = 0

jogador['Nome'] = input('Nome do jogador: ').title().strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for j in range(0, partidas): # descobrir a quantidade de gols por partida
    gol = int(input(f'Quantos gols na partida {j + 1}? '))
    gols.append(gol)
    sgols += gol

jogador['Gols'] = gols[:]
jogador['Total de gols'] = sgols
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas. ')
for p in range(0, partidas): # mostrando novamento a quantidade de gols por partida do jogador
    print(f'    => Na partida {p + 1}, fez {gols[p]} gols.')
print(f'Foi um total de {jogador["Total de gols"]} gols.')
