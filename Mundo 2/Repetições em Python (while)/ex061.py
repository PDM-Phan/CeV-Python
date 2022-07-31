print('10 termos de uma P.A de sua escolha.')

primeiro = int(input('O primeiro termo da P.A: '))
razao = int(input('A razao da P.A: '))
termo = 1
pvalor = primeiro

while termo <= 10:
    print('{}'.format(pvalor), end='')
    print(' -> ', end='')
    termo += 1
    pvalor += razao

print('Finalizado.')
