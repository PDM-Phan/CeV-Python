matriz = [[] , [] , []]
         #0    #1   #2
linha = coluna = somap = 0

for m in range(0, 9):
    pos = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    if pos % 2 == 0: # soma dos valores pares
        somap += pos
    if linha == 0:
        matriz[0].append(pos)
    elif linha == 1:
        matriz[1].append(pos)
    elif linha == 2:
        matriz[2].append(pos)
    coluna += 1
    if coluna > 2:
        linha += 1
        coluna = 0

print('-=' * 20)
soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2] # soma dos valores da 3 coluna

for m in matriz:
    print(f'[ {m[0]:^5} ] [ {m[1]:^5} ] [ {m[2]:^5} ]')

print(f'A soma de todos os valores pares digitados sera: {somap}')
print(f'A soma de todos os valores da terceira coluna sera: {soma3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}') # maior numero da 2 linha