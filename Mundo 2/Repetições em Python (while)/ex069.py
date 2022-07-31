maioridade = 0 # pessoas maiores de 18 anos
totmuie = 0 # mulheres com menos de 20 anos
quanthomi = 0 # quantidade de homens
totpessoas = 0 # quantidade de pessoas gerais
quantmuie = 0 # quantidade de mulheres

while True:
    print('-' * 30)
    print('Cadastre uma pessoa')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    while sexo not in 'mf': # caso digite outra coisa alem de m ou f
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 30)
    totpessoas += 1
    if idade >= 18:
        maioridade += 1 # adicionar numero de maior idade
    if sexo == 'f':
        quantmuie += 1 # adicionar ao numero de muie
    if sexo == 'm':
        quanthomi += 1 # adiciona ao numero de homi
    elif sexo == 'f' and idade < 20:
        totmuie += 1
    esc = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
    if esc == 'n':
        break
    while esc not in 'sn': # caso digite alguma coisa alem de s ou m
        esc = str(input('Quer continuar?[S/N] ')).strip().lower()[0]

print('======= FIM DO PROGRAMA ========')
print('De {} pessoas cadastradas, {} sao maiores de 18 anos.'.format(totpessoas, maioridade))
print('De {} pessoas cadastradas, {} sao homens.'.format(totpessoas, quanthomi))
print('De {} mulheres cadastradas, {} sao menores de 20 anos.'.format(quantmuie, totmuie))