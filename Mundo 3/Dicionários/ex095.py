from time import sleep
totjogadroes = [] # Lista com todos os jogadores

while True:
    jogador = {} # ficha de cada jogador
    gols = [] # lista com todos os jogos
    sgols = 0 # total de gols
    jogador['Nome'] = input('Nome do jogador: ').title().strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for j in range(0, partidas):
        gol = int(input(f'  Quantos gols na partida {j + 1}? '))
        gols.append(gol)
        sgols += gol
    # adcionando os valores a ficha do jogador
    jogador['Gols'] = gols
    jogador['Total de gols'] = sgols
    totjogadroes.append(jogador)
    esc = ' '
    while esc not in 'NS':
        esc = input('Deseja continuar? [S/N] ').upper()
    if esc == 'N':
        print('Cadastrando...')
        sleep(1)
        break
    print('-' * 50)

# tabela com dados gerais de cada jogador
print('-='  * 30)
print(f'{"Cod":<3} {"Nome":<15}{"Gols":<15}{"Total de gols":<3}')
print('-' * 45)
for j in range(0, len(totjogadroes)):
    print(f'{str(j):>3} {str(totjogadroes[j]["Nome"]):<15}{str(totjogadroes[j]["Gols"]):<15}{str(totjogadroes[j]["Total de gols"]):<3}')
print('-' * 45)

# dados especificos de cada jogador
while True:
    op = int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    if op in range(0, len(totjogadroes)): # se o valor de op for dentro da len
        print(f'-- LEVANTAMENTO DO JOGADOR {totjogadroes[op]["Nome"]}:')
        cont = 1 # valor de jogo
        for g in totjogadroes[op]['Gols']: # pegar cada valor dentro da lista de gols
            print(f'    No jogo {cont} fez {g} gols.')
            cont += 1 # aumentar em um o valor de jogo
            sleep(1)
    elif op == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    else:
        # caso seja digitado um valor q "nao exista"
        print(f'\033[91mERRO!\033[m Nao existe jogador com codigo {op}. Tente novamente.')

print('>> PROGRAMA FINALIZADO <<')
