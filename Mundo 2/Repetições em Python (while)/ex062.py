primeiro = int(input('O primeiro termo da P.A: ')) # primeiro termo
razao = int(input('A razao da P.A: '))
termo = 1 # quantidade de termos
pvalor = primeiro # valores

while termo <= 10: # mostra os 10 termos
    print('{}'.format(pvalor), end='')
    print(' -> ', end='')
    termo += 1
    pvalor += razao
print('PAUSA')
mtermos = int(input('Quantos termos voce quer mostrar a mais? ')) # adicionar novos termos

while mtermos != 0: # condiçao do loop
    mtermos += termo
    while termo < mtermos: # mostra os termos adicionais
        print('{}'.format(pvalor), end='')
        print(' -> ', end='')
        termo += 1
        pvalor += razao
    print('PAUSA')
    mtermos = int(input('Quantos termos voce quer mostrar a mais? '))

# soma dos termos totais
print('Finalizado com {} termos.'.format(termo - 1))

