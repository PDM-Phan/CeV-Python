matriz = [[] , [] , []]
  #linhas 0    #1   #2
linha = coluna = 0 # a posiçao das linhas e das colunas

for m in range(0, 9):
    pos = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    if linha == 0: # enquanto for a primeira linha
        matriz[0].append(pos)
    elif linha == 1: # enquanto for a segunda linha
        matriz[1].append(pos)
    elif linha == 2: # enquanto for a terceira linha
        matriz[2].append(pos)
    coluna += 1
    if coluna > 2: # condiçao para a troca da linha
        linha += 1
        coluna = 0

print('-=' * 20)
for m in matriz: # formaçao da linha
    print(f'[ {m[0]:^5} ] [ {m[1]:^5} ] [ {m[2]:^5} ]')