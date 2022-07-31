somaidade = 0 # soma das idades
mediaidade = 0 # media das 4 idades
maioridadehomem = 0 # maior idade de um HOMEM
nomevelho = '' # nome desse homem
totmulher20 = 0 # total de mulheres com menos de 20 anos

for p in range (1, 5):
    print('-------- {} PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'mM': # determinando valor inicial para o homem mais velho
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: # realizar a troca desse valor
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20: # determinar mulheres menores de 20 anos
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media das idades do grupo é {} anos.'.format(mediaidade))
print('A idade do homem mais velho é {} e seu nome é {}.'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos sao {}.'.format(totmulher20))