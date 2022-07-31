times = ('Flamengo', 'Internacional', 'Atletico-MG', 'Sao Paulo', 'Fluminense', 'Gremio', 'Palmeiras', 'Santos', 'Atletico-PR'
         , 'Brangantino', 'Ceara', 'Corinthinans', 'Atletico Goianinense', 'Bahia', 'Sport', 'Fortaleza EC', 'Vasco da Gama',
         'Goias', 'Coritiba', 'Botafogo') # lista de times
print(f'TABELA DO BRASILEIRAO: {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados sao, respectivamente: {times[0:5]}') # separando os primeiros 5 colocados
print('-=' * 20)
print(f'Os 4 ultimos times sao, respectivamente: {times[-4:]}') # separando os 4 ultimos colocados
print('-=' * 20)
print(f'Se colocarmos a lista de times em ordem alfabetica, ficara desse jeito: {sorted(times)}') # em ordem alfabetica
print('-=' * 20)
print(f'A Bahia esta na {times.index("Bahia") + 1} posiçao') # mostrando a colocaçao de um time



