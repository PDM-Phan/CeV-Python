from datetime import date
pessoa = {}
anoatual = date.today().year # determinando o ano atual

pessoa['Nome'] = input('Nome: ').title()
anonascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = anoatual - anonascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho: (0 se nao possui) '))

if pessoa['CTPS'] != 0: # caso possua uma carteira de trabalho
    pessoa['Ano de contrataçao'] = int(input('Ano de contrataçao: '))
    pessoa['Salario'] = float(input('Salario: R$'))
    pessoa['Aposentadoria'] = (pessoa['Ano de contrataçao'] - anonascimento) + 35

print('-=' * 30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
