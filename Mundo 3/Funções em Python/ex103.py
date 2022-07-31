def ficha(nome='<desconhecido>', gols=0):
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
nome = input('Nome do jogador: ').title()
gols = input('Numero de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
