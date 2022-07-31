pessoas = [] # total de pessoas
totmuie = [] # nomes de todas as mulheres
somidades = 0

while True:
    pessoa = {}
    pessoa['Nome'] = input('Nome: ').title()
    while True:
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper()
        if pessoa['Sexo'] == 'F': # se o sexo for F
            totmuie.append(pessoa['Nome'])
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    somidades += pessoa['Idade']
    pessoas.append(pessoa.copy())
    esc = input('Deseja cadastrar mais outra pessoa? [S/N] ').upper()
    while esc not in 'NS':
        esc = input('Por favor digita apenas [S/N]. ').upper()
    if esc == 'N':
        print('Finalizando...')
        break
    print('-' * 50)
print('-=' * 25)
print(f'A) O grupo tem {len(pessoas)} pessoas.')
mediaidades = somidades / len(pessoas)
print(f'B) A media de idades das pessoas cadastradas é de {int(mediaidades)}.')

print(f'C) As mulheres cadastradas foram: ', end=' ')
for t in totmuie:
    print(t, end=' ')
print()

print('D) Pessoas que estao com a idade acima da media: ')
for p in range(0, len(pessoas)):
    if pessoas[p]['Idade'] > mediaidades: # se a idadde da pessoa na posiçao p for maior q a media
        print()
        for k, v in pessoas[p].items():
            print(f'    {k} = {v};', end=' ')
print()
print('<< FINALIZADO >>')
