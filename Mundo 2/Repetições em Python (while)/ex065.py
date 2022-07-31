decisao = 'S' # valor booleano
quantidade = 0 # quantidade de numeros
soma = 0 # soma dos numeros
valores = [] # guardar todos os numeros

while decisao == 'S':
    num = int(input('\033[93mDigite um numero inteiro:\033[m '))
    decisao = str(input('Deseja continuar? \033[94m[S/N]\033[m ')).strip().upper()[0] # confirmar ou n o booleano
    quantidade += 1 # adicionar a variavel
    soma += num # soma dos valores
    valores.append(num) # levar pra lista

media = soma / quantidade # media de todos os valores
valores.sort(key=int) # colocar a lista em ordem crescente

print('A media de todos os \033[4;96m{}\033[m numeros sera de \033[4;96m{}\033[m.'.format(quantidade, media))
print('O maior numero foi \033[4;92m{}\033[m e o menor foi \033[4;91m{}\033[m.'.format(valores[-1], valores[0]))
